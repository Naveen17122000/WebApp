from django.urls import path
from . import views

urlpatterns=[
    path('',views.inheritanceFun),
    path('child/',views.inheritanceChild),
    path('subchild/',views.inheritanceSubChild),
]