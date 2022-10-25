from . import views

from django.urls import path


from .views import GeneratePDF

from django.views.generic.base import TemplateView


urlpatterns = [
    path('project_details', views.project_details, name='project_details'),
    path('project_details_pdf/', GeneratePDF.as_view()),
]