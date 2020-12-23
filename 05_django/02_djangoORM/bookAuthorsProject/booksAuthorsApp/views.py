from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import Book, Author, User

#*************************************************
#                   Log In Methods
#*************************************************
def index(request):
    return render (request, "loginUser.html")


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
    return render(request, "home.html", context)        

def registerUser(request):
    return render(request, "registerUser.html")

def register(request):
    # print(request.POST)
    validationErrors = User.objects.userValidator(request.POST)
    if len(validationErrors)>0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        return redirect ("/registerUser")
    else:
        #encrypt PW thennn create user        
        securePW = bcrypt.hashpw(request.POST["password"].encode(),bcrypt.gensalt()).decode()
        newUser = User.objects.create(firstName = request.POST["fname"], lastName = request.POST["lname"], email = request.POST["email"], password = securePW)
        request.session["loggedInID"] = newUser.id
    return redirect ("/home")


def logout(request):
    request.session.clear()
    return redirect("/")


#*************************************************
#                   Book Methods
#*************************************************
def booksHomepage(request):
    allBooks = Book.objects.all()
    context = {
        'allTheBooks' : allBooks
    }    
    return render(request, "booksHomepage.html", context)

def createBook(request):
    validationErrors = Book.objects.bookValidator(request.POST)
    if len(validationErrors)>0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        return redirect ("/booksHomepage")
    newTitle = Book.objects.create(title = request.POST["title"], desc = request.POST["desc"])   
    return redirect("/booksHomepage")

def showTitle(request, titleID):
    bookToShow = Book.objects.get(id=titleID)
    context = {
        'titleInfo' : bookToShow,
        'allAuthors' : Author.objects.all()
    }    
    return render(request, "showTitle.html", context)
        

def addAuthor(request, bookinfo):
    thisAuthor = Author.objects.get(id=request.POST['authorinfo'])
    thisBook = Book.objects.get(id=bookinfo)
    thisAuthor.books.add(thisBook)
    return redirect(f"/books/{bookinfo}") #can be either return fx depending on where I want it to render
    # return redirect("/")

def deleteBook(request, titleID):   
    b = Book.objects.get(id=titleID)
    b.delete()
    return redirect("/booksHomepage")

def editBook(request, titleID): 
    context = {
        "booktoEdit" : Book.objects.get(id=titleID)
    }    
    return render(request, "edit.html", context)

def updateBook(request, titleID):
    validationErrors = Book.objects.bookValidator(request.POST)
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        # print(validationErrors)
        return redirect(f"/edit/{titleID}")
    u = Book.objects.get(id = titleID)
    u.title = request.POST['title']
    u.desc = request.POST['desc']
    u.save()
    return redirect("/booksHomepage")
#*************************************************
#*************************************************
#                   Author Methods
#*************************************************

def authorsHomepage(request):
    allAuthors = Author.objects.all()
    context = {
        'allTheAuthors' : allAuthors
    }
    return render (request, "authorsHomepage.html", context)

def createAuthor(request):    
    validationErrors = Author.objects.authorValidator(request.POST)
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        # print(validationErrors)
        return redirect ("/authorsHomepage")
    #return is a child of If statement
    newAuthor = Author.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], notes = request.POST['notes'])   
    return redirect ("/authorsHomepage")


def showAuthor(request, authorID):
    authorToShow= Author.objects.get(id=authorID)
    context = {
        "authorinfo" : authorToShow,
        "allBooks" :Book.objects.all()
    }
    return render(request, "showAuthor.html", context)


def addBookToAuthor(request, authorID):
    thisBook = Book.objects.get(id=request.POST['bookinfo'])
    thisAuthor = Author.objects.get(id=authorID)
    thisBook.authors.add(thisAuthor)
    return redirect(f"/author/{authorID}")



def deleteAuthor(request, authorID):
    d = Author.objects.get(id=authorID)
    d.delete()
    # return redirect(f"/author/{authorID}")
    return redirect("/authorsHomepage")

def editAuthorpage(request, authorID):
    context = {
        "editAuthor" : Author.objects.get(id=authorID)
    }
    return render(request, "editAuthor.html",context)


def updateAuthor(request, authorID):
    validationErrors = Author.objects.authorValidator(request.POST)
    if len(validationErrors) > 0:
        for key, value in validationErrors.items():
            messages.error(request,value)
        print('*'*50)
        print(validationErrors)
        return redirect (f"/editAuthor/{authorID}")
    u = Author.objects.get(id = authorID)
    u.fname = request.POST['fname']
    u.lname = request.POST['lname']
    u.notes = request.POST['notes']
    u.save()
    return redirect ("/authorsHomepage")
    





