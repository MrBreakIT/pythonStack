from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    print("----------<<<  Start of Result method  >>>----------")
    nameFromForm = request.POST["name"]
    locationFromForm = request.POST['location']
    languageFromForm = request.POST['language']
    commentFromForm = request.POST['comment']
    context = {
        "nameOnTemplate" : nameFromForm,
        "locationOnTemplate" : locationFromForm,
        "languageOnTemplate": languageFromForm,
        "commentOnTemplate" : commentFromForm
    }
    print(request.POST) 
    print("----------<<<  End of Result method  >>>----------")
    return render(request, "success.html", context)

# def success (request):
#     return render(request, "success.html", context)











