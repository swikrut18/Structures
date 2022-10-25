from django.shortcuts import render


from django.http import HttpResponse

from .utils import render_to_pdf
from django.template.loader import get_template
from django.views.generic.base import TemplateView
from django.utils.datastructures import MultiValueDictKeyError

        
def index(request):

    global m1
    global m2
    global m3
    global m4
    global m5
    global m6
    global m7
    global m8
    global m9
    global m10
    global m11
    global m12
    global m13
    global m14
    global m15
    global m16
    global m17
    global m18
    global m19
    global m20
    global m21
    global m22
    global m23
    global m24
    global m25
    global m26
    global m27
    global m28

    try:
        m1 = str(request.GET['nun1'])
        m2 = str(request.GET['nun2'])
        m3 = str(request.GET['nun3'])
        m4 = str(request.GET['nun4'])
        m5 = str(request.GET['nun5'])
        m6 = str(request.GET['nun6'])
        m7 = str(request.GET['nun7'])
        m8 = str(request.GET['nun8'])
        m9 = str(request.GET['nun9'])
        m11 = str(request.GET['nun11'])
        m12 = str(request.GET['nun12'])
        m13 = str(request.GET['nun13'])
        m14 = str(request.GET['nun14'])
        m15 = str(request.GET['nun15'])
        m16 = str(request.GET['nun16'])
        m17 = str(request.GET['nun17'])
        m18 = str(request.GET['nun18'])
        m19 = str(request.GET['nun19'])
        m20 = str(request.GET['nun20'])
        m21 = str(request.GET['nun21'])
        m22 = str(request.GET['nun22'])
        m23 = str(request.GET['nun23'])
        m24 = str(request.GET['nun24'])
        m25 = str(request.GET['nun25'])
        m26 = str(request.GET['nun26'])
        m27 = str(request.GET['nun27'])
        m28 = str(request.GET['nun28'])

    except MultiValueDictKeyError:
        m1 = str()
        m2 = str()
        m3 = str()
        m4 = str()
        m5 = str()
        m6 = str()
        m7 = str()
        m8 = str()
        m9 = str()
        m11 = str()
        m12 = str()
        m13 = str()
        m14 = str()
        m15 = str()
        m16 = str()
        m17 = str()
        m18 = str()
        m19 = str()
        m20 = str()
        m21 = str()
        m22 = str()
        m23 = str()
        m24 = str()
        m25 = str()
        m26 = str()
        m27 = str()
        m28 = str()
    return render(request, 'index/index.html')


class GeneratePDF(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template = get_template('index/index_pdf.html')
        context = {
           
           "a1": m1,
           "a2": m2,
           "a3": m3,
           "a4": m4,
           "a5": m5,
           "a6": m6,
           "a7": m7,
           "a8": m8,
           "a9": m9,
           "a11": m11,
           "a12": m12,
           "a13": m13,
           "a14": m14,
           "a15": m15,
           "a16": m16,
           "a17": m17,
           "a18": m18,
           "a19": m19,
           "a20": m20,
           "a21": m21,
           "a22": m22,
           "a23": m23,
           "a24": m24,
           "a25": m25,
           "a26": m26,
           "a27": m27,
           "a28": m28
        }
        

        html = template.render(context)
   
        pdf = render_to_pdf('index/index_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')



