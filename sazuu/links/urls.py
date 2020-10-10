from django.urls import path

from . import views

urlpatterns = [
    path('', views.LinkListView.as_view(), name='links'),
    path('<int:pk>/redirect', views.redirect_link, name='redirect_link')
]