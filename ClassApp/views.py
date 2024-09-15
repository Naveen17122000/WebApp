from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from ProductApp.models import Product
from .models import Employee

# Create your views here.
class FirstCBV(View):
    def get(self,request):
        #return HttpResponse('classApp has recived get request')
        return render(request,'ClassApp/class.html')
    
    def post(self,request):
        data = request.POST['t1']
        return render(request,'ClassApp/class.html',{'data':data})

class SecondCBV(FirstCBV):
    
    def post(self, request):
        return HttpResponse('Inherited to secondCBV')
    
class ProductList(ListView):
    model = Employee

class ProductCreate(CreateView):
    #model = Product
    model = Employee
    fields = '__all__'
    
    def get_success_url(self):
        return reverse('productcbvurl')

class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'ClassApp/empupdate.html'

    def get_success_url(self) -> str:
        return reverse('productcbvurl')

class DeleteEmployee(DeleteView):
    model = Employee
    template_name='ClassApp/empdelete.html'

    def get_success_url(self):
        return reverse('productcbvurl')
