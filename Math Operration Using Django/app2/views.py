from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showadd(request):
    x=request.POST.get('fno')
    y=request.POST.get('sno')
    a=int(x)
    b=int(y)
    add=a+b
    return render(request,"index.html",{"add":add})


def showsub(request):
    x = request.POST.get('fno')
    y = request.POST.get('sno')
    a = int(x)
    b = int(y)
    sub = a - b
    return render(request,"index.html",{"sub":sub})


def showmul(request):
    x = request.POST.get('fno')
    y = request.POST.get('sno')
    a = int(x)
    b = int(y)
    mul = a * b
    return render(request,"index.html",{"mul":mul})


def showdiv(request):
    x = request.POST.get('fno')
    y = request.POST.get('sno')
    a = int(x)
    b = int(y)
    div = a / b
    return render(request,"index.html",{"div":div})