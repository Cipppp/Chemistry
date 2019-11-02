from django.urls import path
from . import views

urlpatterns = [
    path('alcoolul/', views.home, name = "alcoolul-home"),
    path('alcoolul/metanol/', views.metanol, name = "metanol-home"),
    path('alcoolul/etanol/', views.etanol, name = "etanol-home"),
    path('alcoolul/glicerol/', views.glicerol, name = "glicerol-home"),


]