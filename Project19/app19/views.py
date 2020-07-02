from django.shortcuts import render
from .models import EmpolyeeModel


def showIndex(request):
    return render(request,"index.html")


def showNew(request):
    return render(request,"newemployee.html")


def showSave(request):
    idno=request.POST.get("id")
    name=request.POST.get("na")
    gender=request.POST.get("male")
    salary=request.POST.get("sal")
    doj=request.POST.get("doj")
    em=EmpolyeeModel(id=idno,name=name,gender=gender,sal=salary,doj=doj)
    em.save()
    return render(request,"newemployee.html", {"message":"Data Inserted Successfully"})


def showView(request):
    return render(request,"viewemployee.html")

