from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import render,redirect
from IHAModule.models import IHA
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required,login_required
from HiringModule.models import Hiring
from django.contrib import messages


@api_view(['POST','GET'])
@login_required
@permission_required('IHAModule.view_iha',login_url='/auth/login')
def iha_list(request):
    try:
        all_iha = IHA.objects.all()
        messages.info(request, "İhalar başarıyla listelendi")
        return render(request, 'iha-list.html',{'all_iha':all_iha})
    except:
        messages.error(request, "İhalar listelenirken bir hata meydana geldi")


@api_view(['POST','GET'])
@login_required
@permission_required('IHAModule.add_iha',login_url='/auth/login')
def iha_add(request):
    try:
        if request.method == 'POST':
            brand = request.data.get('brand')
            model = request.data.get('model')
            weight = request.data.get('weight')
            category = request.data.get('category')
            iha = IHA(brand=brand, model=model, weight=weight, category=category)
            iha.save()
            messages.success(request, "İha başarı ile eklendi")
            return redirect('/iha/list')
        return render(request, 'iha-add.html')

    except:
        messages.error(request, "İha eklenirken bir hata meydana geldi")
        return render(request, 'iha-add.html')


@api_view(['POST','GET'])
@login_required
@permission_required('IHAModule.change_iha',login_url='/auth/login')
def iha_update(request,id):

    try:
        iha = IHA.objects.get(id=id)
        if request.method == 'POST':
            iha.brand = request.data.get('brand')
            iha.model = request.data.get('model')
            iha.weight = request.data.get('weight')
            iha.category = request.data.get('category')
            iha.save()
            messages.success(request, "İha başarı ile güncellendi")

            return redirect('/iha/list')
        return render(request, 'iha-update.html',{'iha':iha})
    except:
        messages.error(request, "İha güncellenirken bir hata meydana geldi")
        return render(request, 'iha-update.html',{'iha':iha})



@api_view(['DELETE'])
@login_required
@permission_required('IHAModule.delete_iha',login_url='/auth/login')
def iha_delete(request,id):
    try:
        iha = IHA.objects.get(id=id)

    except IHA.DoesNotExist:
        messages.error(request,"Kayıtlı iha bulunamadı")
        return Response(status=404)
    
    if Hiring.objects.filter(iha=iha).exists():
        # aktif olarak kiralık durumda ise silinmesini engeller
        if Hiring.objects.filter(iha=iha, end_date_time__gte=timezone.now()).exists():
            messages.warning(request,"İha aktif olarak kiralık durumda olduğu için silinemez.")
            return Response(status=403) 

    iha.delete()
    return Response(status=204)

@api_view(['GET'])
def iha_detail(request,id):
    try:
        iha = IHA.objects.get(id=id)
        messages.success(request, "İha başarı ile getirildi")

        return render(request, 'iha-detail.html',{'iha':iha})
    except:
        messages.error(request, "İha bilgileri getirilirken bir hata meydana geldi")
        return redirect(request, 'iha-list.html')

        