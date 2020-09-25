from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Link

class LinkListView(ListView):
    """
    List all links stored in the database.
    """
    template_name = 'links/link_list.html'
    context_object_name = 'link_list'
    queryset = Link.objects.all()