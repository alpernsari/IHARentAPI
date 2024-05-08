from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.iha_list, name=''),
    path('add/', views.iha_add, name='iha_add'),
    path('update/<int:id>/', views.iha_update, name='iha_update'),
    path('delete/<int:id>', views.iha_delete, name='iha_delete'),
    path('get_list/', views.iha_get_list, name='get_list')
]