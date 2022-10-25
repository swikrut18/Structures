from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('front_page', views.front_page, name='front_page'),
    path('front_page1', views.front_page1, name='front_page1'),
    path('front_page_pdf/', GeneratePDF.as_view()),


    
   
]