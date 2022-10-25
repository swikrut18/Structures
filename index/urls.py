from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('index', views.index, name='index'),
    path('index_pdf/', GeneratePDF.as_view()),
]