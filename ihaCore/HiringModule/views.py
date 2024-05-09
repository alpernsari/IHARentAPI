from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect,get_object_or_404
from HiringModule.models import Hiring
from django.http import JsonResponse
from IHAModule.models import IHA
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib import messages


#Tüm kiralamaların listelenmesi (admin)
@api_view(['POST','GET'])
@login_required
@permission_required('HiringModule.admin_list_hiring',login_url='/hiring/user-list')
def hiring_list(request):
    all_hirings = Hiring.objects.select_related('iha', 'user').all()
    return render(request, 'admin-hiring-list.html',{'all_hirings':all_hirings})

# iha kiralama metodu admin ve user kullanabilir
@api_view(['POST','GET'])
@login_required
@permission_required('HiringModule.add_hiring',login_url='/auth/login')
def hire_iha(request):
    all_ihas = IHA.objects.all()
    #post geldiyse ekleme işlemi
    if request.method == "POST":
        # form gelen değerler ile bir hiring nesnesi oluşturulur
        iha_id = request.data.get("ihas")
        start_date = request.data.get("start_date_time")
        end_date = request.data.get("end_date_time")

        #kiralama başlangıç tarihi bitiş tarihinden sonraysa uyarı mesajı
        if start_date> end_date:
            messages.warning(request,"Kiralama başlangıç tarihi, bitiş tarihinden sonra olamaz")
            return render(request,'hiring-iha.html',{'all_ihas' : all_ihas})
        
        user_id = request.user.id
        hiring = Hiring(iha_id = iha_id,
                        start_date_time = start_date,end_date_time = end_date,
                        user_id = user_id
                        )
        hiring.save()

        return redirect("/hiring/user-list")
    else:
        
        return render(request,'hiring-iha.html',{'all_ihas' : all_ihas})

@api_view(['DELETE'])
@login_required
@permission_required('HiringModule.admin_delete',login_url='/auth/login')
def hiring_delete(request,id):
    try:
        hiring = Hiring.objects.get(id=id)
    except Hiring.DoesNotExist:
        messages.error(request, "Kayıtlarda böyle bir kiralama bulunamadı")  
        return Response(status=403)
    
    
    hiring.delete()
    messages.success(request,"Başarı ile kaldırıldı")
    return Response(status=200)



@api_view(['POST','GET'])
@login_required
@permission_required('HiringModule.admin_update',login_url='/auth/login')
def hiring_update(request,hiring_id):

    hiring = Hiring.objects.get(id=hiring_id)
    #dropdown da gösterebilmek için ihalar çekilir
    all_ihas = IHA.objects.all()
    if request.method == 'POST':
        hiring.iha_id = request.data.get('ihas')
        hiring.start_date_time = request.data.get('start_date_time')
        hiring.end_date_time = request.data.get('end_date_time')
        hiring.save()
        return redirect('/hiring/admin-hiring-list')
    else:
        return render(request,"admin-hiring-update.html",{'hiring': hiring,'all_ihas':all_ihas})
    
#user liste çekme
@api_view(['POST','GET'])
@login_required
@permission_required('HiringModule.user_list_hiring',login_url='/auth/login')
def user_hiring_list(request):
    user_id = request.user.id
    user_hirings = Hiring.objects.filter(user_id = user_id)
    return render(request, 'user-hiring-list.html',{'user_hirings':user_hirings})

@api_view(['POST','GET'])
@login_required
@permission_required('HiringModule.user_update',login_url='/auth/login')
def user_hiring_update(request,hiring_id):
        hiring = Hiring.objects.get(id=hiring_id)
        all_ihas = IHA.objects.all()
        if request.method == 'POST':
            hiring.iha_id = request.data.get('ihas')
            hiring.start_date_time = request.data.get('start_date_time')
            hiring.end_date_time = request.data.get('end_date_time')
            hiring.save()
            return redirect('/hiring/user-list')
        else:
            return render(request,"user-hiring-update.html",{'hiring': hiring,'all_ihas':all_ihas})

@api_view(['DELETE'])
@login_required
@permission_required('HiringModule.user_delete',login_url='/auth/login')
def user_hiring_delete(request,id):
    try:
        hiring = Hiring.objects.get(id=id)
        if hiring.user_id != request.user.id:
            redirect('/hiring/user-list')
    except Hiring.DoesNotExist:
        return Response(status=404)  
    
    hiring.delete()
    return Response(status=204)