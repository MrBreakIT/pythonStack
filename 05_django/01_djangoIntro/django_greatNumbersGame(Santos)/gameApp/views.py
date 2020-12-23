from django.shortcuts import render, redirect
import random

def index(request):
    if "number" not in request.session:
        request.session["number"] = random.randint(1,10)
    print("Computer chose:", request.session["number"])
    return render(request,"index.html")

def guess(request):
    request.session["guess"] = int(request.POST["guess"])
    if request.session["guess"] > request.session["number"]:
        request.session['alert'] = "Too high"
    elif request.session["guess"] < request.session["number"]:
        request.session['alert'] = "Too low"
    elif request.session["guess"] == request.session["number"]:
        request.session['alert'] = "right on target"
    return redirect('/')

def reset(request):
    # del request.session["guess"]
    # del request.session["number"]
    request.session.flush()
    return redirect('/')