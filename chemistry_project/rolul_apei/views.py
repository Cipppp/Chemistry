from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'rolul_apei/home.html')


# Create your views here.
