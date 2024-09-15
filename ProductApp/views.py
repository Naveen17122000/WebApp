from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ProductForm
from . forms import CreateForm
from . models import Product
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator
#from django.contrib.auth.forms import UserCreationFor
# Create your views here.
x = 0
def insertProduct(request):
    productform = ProductForm()
    if request.method == 'POST':
        dataForm = ProductForm(request.POST,request.FILES)
        if dataForm.is_valid():
            dataForm.save()
            messages.success(request,'Product is inserted Successfully')
            return redirect('inserturl')
        else:
            messages.error(request,'Product inserting is failed')
            return render(request,'ProductApp/product.html',{'form':dataForm})
    return render(request,'ProductApp/product.html',{'form':productform})

@login_required(login_url = 'loginurl')
def selectProduct(request,pageno=1):
    products = Product.objects.all()
    pageObj = Paginator(products,2) 
    page = pageObj.get_page(pageno) 
    return render(request,'ProductApp/select.html',{'Product':page})

@user_passes_test(lambda user:user.is_staff,login_url='loginurl')
@login_required(login_url = 'loginurl')
def detailFuntion(request,pid):
    request.session.modified = True
    if 'prev_prds' in request.session:
        request.session['prev_prds'].append(pid)
    else:
        request.session['prev_prds'] = [pid]

    product = Product.objects.get(pid=pid)
    Prev_prds = Product.objects.filter(pid__in = request.session['prev_prds'])
    print(request.session['prev_prds'])
    return render(request,'ProductApp/detail.html',{'product':product,'prevPrevs':Prev_prds})

def sessionFunction(request):
    request.session.modified = True
    if 'x' in request.session:
        request.session['x']+=1
    else:
        request.session['x'] = 1

    return HttpResponse('Request no '+str(request.session['x']))

def loginUser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        validUser = authenticate(request,username = uname,password = pwd)
        if validUser != None:
            login(request,validUser)
            return redirect('homeurl',pageno=1)
        else:
            messages.error(request,'Invalid credentials')
            return render(request,'ProductApp/login.html')
    else:
        return render(request,'ProductApp/login.html')
    
def logoutUser(request):
    logout(request)
    return render(request,'ProductApp/login.html')

def signupUser(request):
    emptyForm = CreateForm()
    if request.method == 'POST':
        dataForm = CreateForm(request.POST)
        if dataForm.is_valid() == True:
            dataForm.save()
            return redirect('loginurl')
        else:
            print(dataForm.errors)
            return render(request,'ProductApp/signup.html',{'form':dataForm})
    return render(request,'ProductApp/signup.html',{'form':emptyForm})