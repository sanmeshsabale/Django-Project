from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def savedata(request):
    name=request.POST.get("na")
    contact=request.POST.get("con")
    address=request.POST.get("add")
    room=request.POST.get("r1")
    amm=request.POST.getlist("c1")
    if room == "Ordinary":
        charge = 1500
    elif room == "Deluxe":
        charge = 2500
    elif room == "Suite Room":
        charge = 5000

    chrg = 0

    for x in amm:
        chrg += int(x)

    total = charge + chrg


    d1={"total":total,"name":name,"contact":contact,"address":address,"room":room,"amm":amm,"charge":charge,"chrg":chrg}
    return render(request,"show.html",d1)