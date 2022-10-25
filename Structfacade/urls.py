from django.urls import path

from . import views



urlpatterns = [
    path('structfacade', views.structfacade, name='structfacade'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('services', views.services, name='services'),
]

