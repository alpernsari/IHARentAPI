from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect,get_object_or_404
from IHAModule.models import IHA
from django.http import JsonResponse

@api_view(['POST','GET'])
def iha_list(request):
    all_iha = IHA.objects.all()
    return render(request, 'iha-list.html',{'all_iha':all_iha})

@api_view(['POST','GET'])
def iha_add(request):

    if request.method == 'POST':
        brand = request.data.get('brand')
        model = request.data.get('model')
        weight = request.data.get('weight')
        category = request.data.get('category')
        iha = IHA(brand=brand, model=model, weight=weight, category=category)
        iha.save()
        return redirect('')
    return render(request, 'iha-add.html')


@api_view(['POST','GET'])
def iha_update(request,id):

    iha = IHA.objects.get(id=id)
    if request.method == 'POST':
        iha.brand = request.data.get('brand')
        iha.model = request.data.get('model')
        iha.weight = request.data.get('weight')
        iha.category = request.data.get('category')
        iha.save()
        return redirect('')
    return render(request, 'iha-update.html',{'iha':iha})


@api_view(['DELETE'])
def iha_delete(request,id):
    try:
        iha = IHA.objects.get(id=id)
    except IHA.DoesNotExist:
        return Response(status=404)  # Return a 404 response if the object doesn't exist
    
    iha.delete()
    return Response(status=204)

@api_view(['GET'])
def iha_get_list(request):
    print("*********************************************************")
    all_iha = IHA.objects.all()
    return JsonResponse({'all_iha':list(all_iha.values())})
        