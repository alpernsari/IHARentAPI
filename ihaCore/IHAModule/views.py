from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect,get_object_or_404
from IHAModule.models import IHA
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required,login_required


@api_view(['POST','GET'])
@login_required
@permission_required('IHAModule.view_iha',login_url='/auth/login')
def iha_list(request):
    all_iha = IHA.objects.all()
    return render(request, 'iha-list.html',{'all_iha':all_iha})

@api_view(['POST','GET'])
@login_required
@permission_required('IHAModule.add_iha',login_url='/auth/login')
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
@login_required
@permission_required('IHAModule.change_iha',login_url='/auth/login')
def iha_update(request,id):

    iha = IHA.objects.get(id=id)
    if request.method == 'POST':
        iha.brand = request.data.get('brand')
        iha.model = request.data.get('model')
        iha.weight = request.data.get('weight')
        iha.category = request.data.get('category')
        iha.save()
        return redirect('/iha/list')
    return render(request, 'iha-update.html',{'iha':iha})


@api_view(['DELETE'])
@login_required
@permission_required('IHAModule.delete_iha',login_url='/auth/login')
def iha_delete(request,id):
    try:
        iha = IHA.objects.get(id=id)
        
    except IHA.DoesNotExist:
        return Response(status=404)  # Return a 404 response if the object doesn't exist
    
    iha.delete()
    return Response(status=204)

@api_view(['GET'])
def iha_detail(request,id):
    iha = IHA.objects.get(id=id)
    return render(request, 'iha-detail.html',{'iha':iha})
        