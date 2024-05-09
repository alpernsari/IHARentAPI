from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.hiring_list, name='hiring_list'),
    path('user-list/', views.user_hiring_list, name='user_list'),
    path('user-list/add/', views.hire_iha, name='hiring_add'),
    path('update/<int:hiring_id>/', views.hiring_update, name='hiring_update'),
    path('user-list/update/<int:hiring_id>/', views.user_hiring_update, name='user_hiring_update'),
    path('delete/<int:id>', views.hiring_delete, name='hiring_delete'),
    path('user-list/delete/<int:id>', views.user_hiring_delete, name='user_hiring_delete'),
]