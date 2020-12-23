from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import Book, Author, User

#*******************************************************
#                       Log in/Register Page
#*******************************************************
def index(request):
    return render(request, "index.html")

def registerUser(request):
    # print(request.POST)
    validationErrors = User.objects.userValidator(request.POST)
    if len(validationErrors)>0:
        for key, value in validationErrors.items():
            messages.error(request,value)
            print(request.POST)
            print(validationErrors)
        return redirect ("/")
    else:
        #encrypt PW thennn create user        
        securePW = bcrypt.hashpw(request.POST["password"].encode(),bcrypt.gensalt()).decode()
        newUser = User.objects.create(firstName = request.POST["fname"], lastName = request.POST["lname"], email = request.POST["email"], password = securePW)
        request.session["loggedInID"] = newUser.id
    return render (request, "userHomepage.html")

def login(request):
    # print(validationErrors)    
    validationErrors = User.objects.loginValidator(request.POST)
    if len(validationErrors)>0:
        for value in validationErrors.values():
            messages.error(request,value) 
            print(validationErrors)       
        return redirect ("/")
    else:
        usersEmail = User.objects.filter(email = request.POST["email"]) 
        request.session["loggedInID"] = usersEmail[0].id
        return redirect("/home")

def home(request):
    if "loggedInID" not in request.session:
        messages.error(request, "You must log in first.")
        return redirect("/")
    context = {
        "loggedinuser" : User.objects.get(id = request.session["loggedInID"])
    }
    print(request.session["loggedInID"])
    return render(request, "userHomepage.html", context) 

def logout(request):
    request.session.clear()
    return redirect("/")

#*******************************************************
#                     Books Homepage
#*******************************************************
def addBook_Review(request):
    allBooks = Book.objects.all()
    context = {
        'allTheBooks' : allBooks
    }
    return render(request, "AddBookReview.html", context)


def createBook_Review(request):
    validationErrors = Book.objects.bookValidator(request.POST)
    if len(validationErrors)>0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        return redirect ("/addBook_Review")
    newTitle = Book.objects.create(title = request.POST["title"], desc = request.POST["review"])   
    return redirect("AddBookReview.html")






