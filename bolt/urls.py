from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('connections', views.connections, name='connections'),
    path('bolt', views.bolt, name='bolt'),
    path('bolt_pdf/', GeneratePDF.as_view()),


    
   
]