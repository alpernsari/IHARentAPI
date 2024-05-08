from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

url_patterns = [
    path('', views.home, name='home')
]