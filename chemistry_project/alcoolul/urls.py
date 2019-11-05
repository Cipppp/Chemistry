from django.urls import path
from . import views

urlpatterns = [
    path('alcoolul/', views.home, name = "alcoolul-home"),
    path('metanol/', views.metanol, name = "metanol-home"),
    path('etanol/', views.etanol, name = "etanol-home"),
    path('glicerol/', views.glicerol, name = "glicerol-home"),


]