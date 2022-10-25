from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [

    path('standard_software_pdf/', GeneratePDF.as_view()),

    
   
]