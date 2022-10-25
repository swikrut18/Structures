from django.shortcuts import render


from django.http import HttpResponse





def structfacade(request):
	return render(request, 'structfacade/structfacade.html')

def aboutus(request):
	return render(request, 'structfacade/aboutus.html')


def services(request):
	return render(request, 'structfacade/services.html')