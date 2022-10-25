from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError




def project_details(request):

    global o1
    global o2
    global o3
    global o4
    global o5
    global o6
    global o7
    global o8
    global o9
    global o10
    global o11
    global o12

    try:
        o1 = str(request.GET['nun1'])
        o2 = str(request.GET['nun2'])
        o3 = str(request.GET['nun3'])
        o4 = str(request.GET['nun4'])
        o5 = str(request.GET['nun5'])
        o6 = str(request.GET['nun6'])
        o7 = str(request.GET['nun7'])
        o8 = str(request.GET['nun8'])
        o9 = str(request.GET['nun9'])
        o10 = str(request.GET['nun10'])
        o11 = str(request.GET['nun11'])
        o12 = str(request.GET['nun12'])

      

    except MultiValueDictKeyError:
        o1 = str()
        o2 = str()
        o3 = str()
        o4 = str()
        o5 = str()
        o6 = str()
        o7 = str()
        o8 = str()
        o9 = str()
        o10 = str()
        o11 = str()
        o12 = str()

    return render(request, 'project_details/project_details.html')


class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('project_details/project_details_pdf.html')
        context = {
           
           "a1": o1,
           "a2": o2,
           "a3": o3,
           "a4": o4,
           "a5": o5,
           "a6": o6,
           "a7": o7,
           "a8": o8,
           "a9": o9,
           "a10": o10,
           "a11": o11,
           "a12": o12,
    
        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('project_details/project_details_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


