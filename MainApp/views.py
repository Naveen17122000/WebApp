from django.shortcuts import render

# Create your views here.
def mainFun(request):
    context={}
    if request.method == 'POST':
        txt = request.POST['t1']
        vowels='aeiouAEIOU'
        v_cnt =0
        c_cnt=0
        
        for ch in txt:
            if ch in vowels:
                v_cnt+=1
            else:
                if ch.isspace != True:
                    c_cnt+=1
        context['vowels'] = v_cnt
        context['consonents'] = c_cnt
        return render(request,'MainApp/result.html',context)

    return render(request,'MainApp/main.html')