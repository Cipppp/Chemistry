from django.urls import path
from . import views

urlpatterns = [
    path('rolul-apei/', views.home, name = "apa-home"),
]