from django.urls import path
from . import views

urlpatterns = [
    path('',views.ormFunction,name='ormurl'),
    path('select/',views.selectEmp,name='selectempurl'),
    path('delete/<int:eno>',views.delete,name='deleteempurl'),
]