from django.shortcuts import render
from .models import Employee
from .serializer import EmpSerialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK
# Create your views here.
'''
@api_view(['GET','POST'])
def SelectData(request):
    if request.method == 'GET':
        empdata = Employee.objects.all()
        empserializer = EmpSerialize(empdata,many=True)
        return Response(empserializer.data)

    if request.method == 'POST':
        empData = request.data
        print(empData)
        edata = EmpSerialize(data = empData,many = True)
        if edata.is_valid() == True:
            edata.save()
            return Response(status = HTTP_201_CREATED)
        else:
            print(edata.errors)
            return Response(status = HTTP_400_BAD_REQUEST)
'''

class SelectEmployee(APIView):
    def get(self,request):
        empdata= Employee.objects.all()
        edata =EmpSerialize(empdata,many = True)
        return Response(edata.data,status = HTTP_200_OK)
    
    def post(self,request):
        empdata = request.data
        edata = EmpSerialize(data=empdata,many=True)
        if edata.is_valid():
            edata.save()
            return Response(status=HTTP_201_CREATED)
        else:
            print(edata.errors)
            return Response(status=HTTP_400_BAD_REQUEST)
    

@api_view(['PUT','DELETE'])
def UpdateEmpData(request,pk):
    exisitingData = Employee.objects.get(empno=pk)

    if request.method == 'PUT':
        empdata = request.data
        emp = EmpSerialize(exisitingData,data = empdata)
        #print(emp)
        if emp.is_valid() == True:
            emp.save()
            return Response(status = HTTP_201_CREATED)
        else:
            print(emp.errors)
            return Response(status= HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        exisitingData.delete()
        return Response(status= HTTP_200_OK)