from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
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
