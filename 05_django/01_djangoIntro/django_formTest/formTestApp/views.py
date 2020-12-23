from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request , "index.html")

def createUser(request):
    print("----------<<< Start of createUser >>>----------")
    nameFromForm = request.POST['userName']
    emailFromForm = request.POST['email']
    context = {
        "nameOnTemplate" : nameFromForm,
        "emailOnTemplate" : emailFromForm
    }
    print(request.POST)
    print("----------<<< End of createUser >>>----------")
    # return redirect("/success")
    return render(request, "success.html", context)

def success(request):
    return render(request, "success.html")










# Create your views here.
