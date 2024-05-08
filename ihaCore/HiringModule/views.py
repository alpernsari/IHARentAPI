from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect,get_object_or_404
from HiringModule.models import Hiring
from django.http import JsonResponse

@api_view(['POST','GET'])
def hiring_list(request):
    all_hirings = Hiring.objects.select_related('iha', 'user').all()
    return render(request, 'hiring-list.html',{'all_hirings':all_hirings})

