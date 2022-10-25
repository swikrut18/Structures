from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError


def dead_load(request):

    global n3
    global n4
    global n5
    global n7
    global n8
    global n9
    global n10
    global n11
    global n12
    global n13
    global n14
    global n15
    global n16
    global n17
    global n18
    global n19
    global n20

    
    try:

        n3 = float(request.GET['num3'])
        n4 = float(request.GET['num4'])
        n5 = float(request.GET['num5'])
        n10 = str(request.GET['num10'])
        n11 = float(request.GET['num11'])
        n12 = float(request.GET['num12'])
        n13 = float(request.GET['num13'])
        n14 = str(request.GET['num14'])


    except MultiValueDictKeyError:
        n3 = float(0)
        n4 = float(0)
        n5 = float(0)
        n10 = str()
        n11 = float(0)
        n12 = float(0)
        n13 = float(0)
        n14 = str()

    # Glass 1
    # Density of the glass
    n7 = 25

    # dead load of the glass
    n1 = n3 * n4 * n5 * n7
    n8 = "{:.2f}".format(n1)

    # dead load on the setting block
    n2 = n1 / 2
    n9 = "{:.2f}".format(n2)

    # glass 2

    # dead load of the glass
    n19 = n11 * n12 * n13 * n7
    n15 = "{:.2f}".format(n19)

    # dead load on the setting block
    n20 = n19 / 2
    n17 = "{:.2f}".format(n20)

    

    return render(request, 'dead_load/dead_load.html', {'fruits': n8})


class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('dead_load/dead_load_pdf.html')
        context = {
           

           "a3": n3,
           "a4": n4,
           "a5": n5,
           "a7": n7,
           "a8": n8,
           "a9": n9,
           "a10": n10,
           "a11": n11,
           "a12": n12,
           "a13": n13,
           "a14": n14,
           "a15": n15,
           "a17": n17,

        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('dead_load/dead_load_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
        
