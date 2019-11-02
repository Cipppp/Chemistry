from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'alcoolul/alcoolul_home.html')

def metanol(request):
	return render(request, 'alcoolul/metanol.html')

def etanol(request):
	return render(request, 'alcoolul/etanol.html')

def glicerol(request):
	return render(request, 'alcoolul/glicerol.html')
# Create your views here.
