from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('header_page', views.header_page, name='header_page'),
    path('header_page_pdf/', GeneratePDF.as_view()),
   
]