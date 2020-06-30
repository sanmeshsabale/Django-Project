from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def validate(request):
    return render(request,"show.html")
