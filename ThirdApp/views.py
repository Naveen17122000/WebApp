from django.shortcuts import render

# Create your views here.
def inheritanceFun(request):
    return render(request,'base.html')
def inheritanceChild(request):
    return render(request,'child.html')
def inheritanceSubChild(request):
    return render(request,'subchild.html')