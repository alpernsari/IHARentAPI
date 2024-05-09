from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views

# Kiralama işleriyle ilgili url ler burda. User ve admin için ayrı url ler bulunuyor
# user, admine özel olan işlemleri gerçekleştiremiyor. başında user yazan url ler user için
# başında herhangi bir şey yazmayan url ler ise adminin erişebildiği url ler için
# admin aynı zamanda user ın erişebildiği tüm url lere erişebilir

urlpatterns = [
    path('list/', views.hiring_list, name='hiring_list'),
    path('user-list/', views.user_hiring_list, name='user_list'),
    path('user-list/add/', views.hire_iha, name='hiring_add'),
    path('update/<int:hiring_id>/', views.hiring_update, name='hiring_update'),
    path('user-list/update/<int:hiring_id>/', views.user_hiring_update, name='user_hiring_update'),
    path('delete/<int:id>', views.hiring_delete, name='hiring_delete'),
    path('user-list/delete/<int:id>', views.user_hiring_delete, name='user_hiring_delete'),
]