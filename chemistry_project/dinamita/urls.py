from django.urls import path
from . import views

urlpatterns = [
    path('dinamita/', views.home, name = "dinamita-home"),
]