from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "main-home"),
    path('elemente-chimice/', views.elemente_chimice, name = "elemente-home"),
    path('rolul-apei/', views.rolul_apei, name = "apa-home"),
    path('chimia-in-alimentatie/', views.chimia_in_alimentatie, name = "alimentatie-home"),
]