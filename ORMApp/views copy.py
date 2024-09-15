from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,Deportment
from django.contrib import messages
from django.core import exceptions
# Create your views here.
def ormFunction(request):
    if request.method == 'POST':
        eno = int(request.POST['eno'])
        ename = request.POST['ename']
        esal = int(request.POST['esal'])
        dno = int(request.POST['dno'])

        #emp = Employee(empno = eno,empname = ename,salary = esal)
        #emp.save()
        try:
            dept = Deportment.objects.filter(deptno=dno)
            if len(dept)>0:
                Employee.objects.create(empno=eno,empname=ename,salary=esal,depotment=dept[0])
                messages.success(request,'Data inserted successfully')
                #return render(request,'ORMApp/empinsert.html')
                #return HttpResponse('Data saved successfully')
                return redirect('selectempurl')
            else:
                messages.error(request,'deportment is not available')
                return render(request,'ORMApp/empinsert.html')
        except Exception:
            messages.error(request,'Error During inserting data')
            return render(request,'ORMApp/empinsert.html')
    
    return render(request,'ORMApp/empinsert.html')
        

def selectEmp(request):
    context={}
    #select * from nk_group2.employee
    emp = Employee.objects.all()
    
    #setofqueries
    context['employees'] = emp
    return render(request,'ORMApp/selectemp.html',context)
    
def delete(request,eno):
    emp = Employee.objects.get(empno=eno)
    emp.delete()
    return redirect('selectempurl')


