from django.urls import path
from .import views

urlpatterns=[
    path('',views.FirstCBV.as_view(),name='classurl'),
    path('second/',views.SecondCBV.as_view(),name='secondurl'),
    path('listcbv/',views.ProductList.as_view(),name='productcbvurl'),
    path('createcbv/',views.ProductCreate.as_view(),name='prdcreateurl'),
    path('updatecbv/<int:pk>',views.UpdateEmployee.as_view(),name='empupdateurl'),
    path('deletecbv/<int:pk>',views.DeleteEmployee.as_view(),name='deletecbvurl')
]