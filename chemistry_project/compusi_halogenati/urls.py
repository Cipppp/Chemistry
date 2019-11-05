from django.urls import path
from . import views

urlpatterns = [
    path('compusi-halogenati/', views.home, name = "compusi-home"),
    path('freon/', views.freon, name = "freon-home"),
    path('distrugerea-stratului/', views.distrugerea, name = "distrugerea-home"),



]