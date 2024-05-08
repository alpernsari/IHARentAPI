from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from IHAModule.tables import IHATable
# Create your views here.

@api_view(['POST','GET'])
def iha_list(request):
    iha = IHATable()
    return render(request, 'iha-list.html',{'iha':iha})