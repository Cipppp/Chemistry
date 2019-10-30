from django.urls import path
from . import  views

urlpatterns = [
	path('elemente-chimice/', views.home, name = "fierul-home"),
	path('magneziul/', views.magneziu_page, name = "magneziul-home"),
	path('siliciul/', views.siliciu_page, name = "siliciul-home"),
	path('manganul/', views.manganul_page, name = "manganul-home"),


]

