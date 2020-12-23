from django.shortcuts import render, redirect
from .models import Users

# Create your views here.
def index(request):
    context = {
        "users_app": Users.objects.all(),
    }
    return render(request, "index.html", context)

def process(request):
    Users.objects.create(fname=request.POST['fname'], lname=request.POST['lname'], email=request.POST['email'], age=request.POST['age'])
    
    return redirect('/')

def deleteUser(request, id):
    print("*****   inside deleteUser   *****")   
    
    u=Users.objects.get(id=id)
    u.delete()
    return redirect('/')





# def deleteUser(request)
#     Users.objects.get()



