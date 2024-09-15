from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.
def display(request):
    #return HttpResponse('Hello NAVEEN welcome to the page')
    return render(request,'first.html')

def readData(request):
    #req = isinstance(request,HttpRequest)
    #resp= HttpResponse('Recevide request '+str(req))
    #return resp
    if request.method =='POST':
        name=request.POST['t1']
        #message = 'Hello Mr.'+name
        #return HttpResponse(message)
        return render(request,'result.html',{'name':name})
    res= render(request,'welcome.html')
    return res
    