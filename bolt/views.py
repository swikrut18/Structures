from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError



def connections(request):
    return render(request, 'bolt/connection.html')


def bolt(request):

    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    
    try:

        n1 = str(request.GET['bol_dia'])
        n1 = n1.upper()
        n2 = str(request.GET['num2'])
        n3 = str(request.GET['num3'])
        n4 = str(request.GET['num4'])
        n5 = str(request.GET['num5'])
        n6 = str(request.GET['num6'])


    except MultiValueDictKeyError:
        n1 = str(6)
        n2 = str(6)
        n3 = str(6)
        n4 = str(6)
        n5 = str(6)
        n6 = str(6)
       

    

    return render(request, 'bolt/bolt.html', {'fruits': n1})


class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('bolt/bolt_pdf.html')
        context = {
           
           "a1": n1,
           # "a2": n2,
           # "a3": n3,
           # "a4": n4,
           # "a5": n5,
           # "a6": n6,
        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('bolt/bolt_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
        







