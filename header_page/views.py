from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError


def header_page(request):
	return render(request, 'header_page/header_page.html')

def header_page(request):

    global n1
    
    try:

        n2 = str(request.GET['num2'])
        n1 = n2.upper()


    except MultiValueDictKeyError:
        n1 = str(0)
       

    

    return render(request, 'header_page/header_page.html', {'fruits': n1})




class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('header_page/header_page_pdf.html')
        context = {
           
           "fruits": n1,
        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('header_page/header_page_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


