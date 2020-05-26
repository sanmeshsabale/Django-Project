from django.shortcuts import render,redirect
from .models import Ass13
from django.contrib import messages


def home(request):
    return render(request, "home.html")


def confirmation(request):
    global name, cno, ch, rd, total
    name = request.POST.get("name")
    cno = request.POST.get("cno")
    ch = request.POST.getlist("ch")
    rd = request.POST.get("rd")

    total = 15000 * len(ch)
    data = {"name": name, "cno": cno, "rd": rd, "ch": ch, "total": total}

    return render(request, "Confirmation.html", data)


def save(request):
    Ass13(name=name, course=ch, type=rd, total=total, cno=cno).save()

    messages.success(request,"Admission Confirm")

    return redirect('home')