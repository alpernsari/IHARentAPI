from django.contrib import admin
from django.urls import path
from django.urls import include, path
from layouts import views as layout_views
from . import views

urlpatterns = [
    path('', views.iha_list, name=''),
    # path('iha-detail/<int:id>', views.iha_detail, name='iha_detail'),
    # path('iha-create', views.iha_create, name='iha_create'),
    # path('iha-update/<int:id>', views.iha_update, name='iha_update'),
    # path('iha-delete/<int:id>', views.iha_delete, name='iha_delete'),
]