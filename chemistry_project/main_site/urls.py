from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "main-home"),
    path('elemente-chimice/', views.elemente_chimice, name = "elemente-home"),
    path('rolul-apei/', views.rolul_apei, name = "apa-home"),
    path('chimia-in-alimentatie/', views.chimia_in_alimentatie, name = "alimentatie-home"),
    path('alcoolul/', views.alcoolul, name = "alcoolul-home"),
    path('compusi-halogenati/', views.compusi_halogenati, name = "compusi-home"),
    path('dinamita/', views.dinamita, name = "dinamita-home"),
]