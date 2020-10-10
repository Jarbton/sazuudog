from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # path('streaming/', views.StreamingView.as_view(), name='streaming'),
    # path('gaming/', views.GamingView.as_view(), name='gaming')
]