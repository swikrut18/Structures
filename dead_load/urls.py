from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('dead_load', views.dead_load, name='dead_load'),
    path('dead_load_pdf/', GeneratePDF.as_view()),
   
]