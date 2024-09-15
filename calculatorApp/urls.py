from django.urls import path
from .import views

urlpatterns=[
    path('',views.CalculatorFun),
    path('mtable/',views.mtableFun),
]