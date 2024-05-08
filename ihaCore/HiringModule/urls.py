from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hiring_list, name=''),
    # path('add/', views.hiring_add, name='hiring_add'),
    # path('update/<int:id>/', views.iha_update, name='hiring_update'),
    # path('delete/<int:id>', views.iha_delete, name='hiring_delete'),
    # path('get_list/', views.iha_get_list, name='get_list')
]