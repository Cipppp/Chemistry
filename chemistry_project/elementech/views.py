from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'elementech/fierul.html')

def magneziu_page(request):
	return render(request, 'elementech/magneziul.html')

def siliciu_page(request):
	return render(request, 'elementech/siliciul.html')


def manganul_page(request):
	return render(request, 'elementech/manganul.html')

