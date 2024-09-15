from django.urls import path
from . import views

urlpatterns=[
    #path('getemployees/',views.SelectData),
    path('getemployees/',views.SelectEmployee.as_view()),
    path('updateemployee/<int:pk>',views.UpdateEmpData),
    path('deleteemployee/<int:pk>',views.UpdateEmpData)
]

