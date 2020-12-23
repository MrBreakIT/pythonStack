from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse

# Create your views here.

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display stuff from all blogs")

def new(request):
    return HttpResponse("placeHolder to display new form to CREATE NEW a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder for blog number {number}")

def edit(request, number):
    return HttpResponse(f"placeholder with EDIT powers {number}")

def destroy(request, number):
    return redirect('/')

def title_content(request):
    return JsonResponse({
        "title": "My first blog", 
        "content": "lorem ipsum blalkbajlj",
    })
    


