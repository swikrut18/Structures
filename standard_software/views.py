from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError








class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('standard_software/standard_software_pdf.html')
        context = {

        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('standard_software/standard_software_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

