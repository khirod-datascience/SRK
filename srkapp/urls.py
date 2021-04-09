from django.contrib import admin
from django.urls import path,include
from srkapp import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("training", views.training, name="training"),
]
