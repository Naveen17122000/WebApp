from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def CalculatorFun(request):
    #return HttpResponse('Calculator app will be received')
    if request.method == 'POST':
        #print(request.POST)
        val1 = int(request.POST['t1'])
        val2 = int(request.POST['t2'])

        if 'add' in request.POST:
            result = val1+val2
            action = 'Addition'
        elif 'subs' in request.POST:
            result = val2-val1
            action = 'Substration'
        elif 'multi' in request.POST:
            result = val1*val2
            action = 'Multipilication'
        
        else:
            result = val2/val1
            action = 'Divisionl'
        return render(request,'calculator.html',{'output':result,'action':action})
    
    return render(request,'calculator.html')

def mtableFun(request):
    context={}
    if request.method =='POST':
        num = int(request.POST['t1'])
        output=[]
        st=''
        for i in range(1,11):
            st = str(num)+' * '+str(i)+' = '+str(i*num)
            output.append(st)
            context['xyz']=output
        return render(request,'mtable.html',context)
    return render(request,'mtable.html')