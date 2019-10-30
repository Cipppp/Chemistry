from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'main_site/home.html')

def rolul_apei(request):
	return render(request, 'rolul_apei/home.html')

def elemente_chimice(request):
	return render(request, 'elementech/fierul.html')

def chimia_in_alimentatie(request):
	return render(request, 'main/home.html')
# Create your views here.
