from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'compusi_halogenati/compusi_halogenati.html')

def freon(request):
	return render(request, 'compusi_halogenati/freon.html')

def distrugerea(request):
	return render(request, 'compusi_halogenati/distrugerea_stratului.html')


# Create your views here.
