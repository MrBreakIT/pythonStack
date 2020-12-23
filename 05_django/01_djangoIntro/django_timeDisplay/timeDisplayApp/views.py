from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime



def index(request):
    context = {
        "date": strftime("%d %B %y"),
        "militaryTime": strftime("%H:%M"),
    }
    return render(request, 'index.html', context)








# Create your views here.
