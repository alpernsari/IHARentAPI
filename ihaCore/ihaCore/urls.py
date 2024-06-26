"""
URL configuration for ihaCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from layouts import views as layout_views
from IHAModule import views as iha_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.sign_in, name='sign_in'),
    path('auth/log_out/', views.log_out, name='log_out'),
    path('home/',layout_views.home, name="home"),
    path('iha/',include('IHAModule.urls')),
    path('hiring/',include('HiringModule.urls')),
]
