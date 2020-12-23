from django.shortcuts import render, redirect
import random

# def index(request):
#     print("---<<<  this is equivalent of flasks' @app.route('/')!  >>>---")
#     print("---<<<  response from index method from root route, localhost:8000!  >>>---")
#     return HttpResponse("this is equivalent of flasks' @app.route('/')!")

def index(request):
    if "number" not in request.session:
        request.session["number"]=random.randint(1,10)
    print("-----<<< Computer chose:", request.session["number"], ">>>-----")
    return render(request, "index.html")

def takeGuess(request):
    request.session["guess"] = int(request.POST["guess"])
    print("-----<<< Start Choices  >>>-----")
    print("   <<< Computer chose:", request.session["number"],">>>   ")
    print("   <<< User chose:", request.session['guess'],">>>   ")
    print("-----<<< End Choices  >>>-----")
    if request.session["guess"] > request.session["number"]:
        request.session['alert'] = "Too High- Computer chose: "
    elif request.session["guess"] < request.session["number"]:
        request.session['alert'] = "Too Low- Computer chose: "
    elif request.session["guess"] == request.session["number"]:
        request.session['alert'] = "Match!"
    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect("/")
