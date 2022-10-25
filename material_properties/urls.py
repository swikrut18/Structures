from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [

    path('material_properties_pdf/', GeneratePDF.as_view()),

    
   
]