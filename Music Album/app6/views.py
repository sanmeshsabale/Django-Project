from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showMain(request):
    return render(request,"show.html")

def showsec(request):
    return render(request,"sec.html")

def showthird(request):
    return render(request,"third.html")