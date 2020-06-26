from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")

def confirmation(request):
    name=request.POST.get("name")
    cnum=request.POST.get("cno")
    classt=request.POST.get("c1")
    course = request.POST.getlist("s1")


    total = 15000 * len(course)
    data = {"name": name, "cno": cnum, "rd": classt, "ch": course, "total": total}

    return render(request, "confirmation.html", data)

def saveDetails(request):
    name=request.POST.get('name')
    cno=request.POST.get("cno")
    classt=request.POST.get("c1")
    course=request.POST.get("s1")
    msg="Data Saved Succssfully"
    return render(request, "confirmation.html", {"mess":msg})
