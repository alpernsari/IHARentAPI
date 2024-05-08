from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect

@api_view(['POST','GET'])
def register(request):
    if request.method == 'POST':
        try:
                
            firstName = request.data.get('firstName')
            lastName = request.data.get('lastName')
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email')

            print(password)

            if User.objects.filter(username=username).exists():
                return Response({'message': 'Kullanıcı kaydı mevcut'})
            # Kullanıcıyı oluştur
            user = User.objects.create_user(username=username, email=email, password=password, 
            first_name=firstName, last_name=lastName)
            user.save()
            return redirect("/auth/register")
        except Exception as e: 
            print(e)

    else:
        return render(request,'register.html')

@api_view(['POST','GET'])
def sign_in(request):

    if request.method == "POST":
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            user = authenticate(username=username, password=password)

            print(user)
            print("*****************************************************************")
            if user is not None:
                login(request,user)
                return redirect('/home')
        except Exception as e:
            print("*************", e)
    else:
        return render(request,'login.html') 

@api_view(['GET'])
def log_out(request):

    logout(request)

    return redirect('/auth/login')