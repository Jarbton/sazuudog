from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Link, Click


class LinkListView(ListView):
    """
    List all links stored in the database.
    """
    template_name = 'links/link_list.html'
    context_object_name = 'link_list'
    queryset = Link.objects.all().order_by('sort_order')


def redirect_link(request, pk):
    link = get_object_or_404(Link, pk=pk)

    click = Click()
    click.link = link
    click.save()

    return HttpResponseRedirect(link.url)


class LinkStatsView(View):
    template_name = 'links/link_stat.html'

    def get(self, request, pk):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('links'))

        link = Link.objects.filter(pk=pk).first()

        dates = []
        number_dates = []
        for click in link.clicks.all():
            click_date = click.created.strftime("%m/%d/%Y")
            if click_date in dates:
                index = dates.index(click_date)
                number_dates[index] += 1
            else:
                dates.append(click_date)
                number_dates.append(1)

        context = {'link' : link}
        context['data'] = number_dates
        context['labels'] = dates

        return render(request, self.template_name, context)
