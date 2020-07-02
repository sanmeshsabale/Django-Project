from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showMain(request):
    salary=float(request.POST.get("esal"))
    da=0.2*salary
    hra=0.4*salary
    total=salary+da+hra
    if total:

        return render(request,"index.html",{"da":da,"hra":hra,"total":total})
    else:
        return render(request, "index.html")




