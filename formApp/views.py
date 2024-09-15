from django.shortcuts import render
from .forms import Formclass
from django.contrib import messages
from . models import Employee
# Create your views here.
def formFunction(request):
    emptyForm = Formclass()
    if request.method == 'POST':
        dataForm = Formclass(request.POST)
        if dataForm.is_valid() == True:
            eno = dataForm.cleaned_data['empno']
            name = dataForm.cleaned_data['empname']
            salary = dataForm.cleaned_data['salary']
            doj = dataForm.cleaned_data['doj']
            gender = dataForm.cleaned_data['gender']
            Employee.objects.create(empno = eno,empname = name,salary = salary,doj = doj,gender= gender)
            return render(request,'formApp/formExp.html',{'name':name,'salary':salary,'form':emptyForm})
        
            messages.success(request,'Data inserted successfully')
            return render(request,'formApp/formExp.html',{'form':emptyForm})

        else:
            messages.error(request,'form is not valid')
            return render(request,'formApp/formExp.html',{'form':dataForm})
    
    return render(request,'formApp/formExp.html',{'form':emptyForm})
