from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('list/', views.iha_list, name='iha_list'),
    path('add/', views.iha_add, name='iha_add'),
    path('update/<int:id>/', views.iha_update, name='iha_update'),
    path('delete/<int:id>', views.iha_delete, name='iha_delete'),
    path('detail/<int:id>', views.iha_detail, name='iha_detail'),
]