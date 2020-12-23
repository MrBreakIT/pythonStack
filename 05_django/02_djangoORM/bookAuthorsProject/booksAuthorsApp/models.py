from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def loginValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        validationErrors = {}
        usersEmail = User.objects.filter(email = postData["email"])       
        if len(postData["email"]) == 0:
            validationErrors["emailreq"] = "User email address required."     
        elif len(usersEmail) == 0:
            validationErrors["emailnotfound"] = "Email not found. Please register first."
            print(validationErrors)
        else:
            userToCheck = usersEmail[0]     #check this against methods... is it usersEmail[0].id?
            if bcrypt.checkpw(postData["password"].encode(), usersEmail[0].password.encode()):
                print("password matches")
            else:
                validationErrors["passwordmatch"] = "Password Incorrect"
            
        return validationErrors


    def userValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        validationErrors = {}
        if len(postData ["fname"]) == 0:
            validationErrors["fnamereq"] = "First Name required."
        if len(postData ["lname"]) == 0:
            validationErrors["lnamereq"] = "Last Name required."
        if len(postData["email"]) < 5:
            validationErrors["emailreq"] = "Valid email address required."
        elif not EMAIL_REGEX.match(postData['email']):
            validationErrors["invalidEmail"] = "Not a valid email address.  Try again."
        else:
            repeatEmail = User.objects.filter(email = postData["email"])
            if len(repeatEmail)>0:
                validationErrors["emailTaken"] = "This email address is already registered."
        if len(postData["password"]) < 5:
            validationErrors["PWreq"] = "Password Required more than 5 characters."
        if postData["password"] != postData ["confirmPW"]:
            validationErrors["confirmError"] = "Passwords do not match."
        return validationErrors

class User (models.Model):
        # id - is implicit when creating models   
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    # books = models.ManyToManyField(
    #     Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()      #this is addition from class AuthorManager
    def __str__(self):
        return f"{self.fname} {self.lname}, {self.email}\n"




class BookManager(models.Manager):
    def bookValidator(self, postData):
        validationErrors = {}
        if len(postData ["title"]) == 0:
            validationErrors["title"] = "Please enter a Book Title"
        if len(postData["desc"]) < 5:
            validationErrors["desc"] = "Please enter the Books Description longer than 5 characters"
        return validationErrors

            
class AuthorManager(models.Manager):
    def authorValidator(self, postData):
        validationErrors = {}
        if len(postData ["fname"]) == 0:
            validationErrors["fname"] = "Please enter Authors first name"
        if len(postData ["lname"]) == 0:
            validationErrors["lname"] = "Please enter a Authors last name"
        if len(postData["notes"]) < 5:
            validationErrors["notes"] = "Please enter a short note about the Author"
        return validationErrors

# Create your models here.
class Book (models.Model):
    # id - is implicit when creating models
    title = models.CharField(max_length=45)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()      #this is addition from class BookManager
    def __str__(self):
        return f"book_object{self.title}\n"

class Author (models.Model):
    # id - is implicit when creating models        
    books = models.ManyToManyField(
        Book, related_name="authors")
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    notes = models.TextField("")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()      #this is addition from class AuthorManager
    def __str__(self):
        return f"{self.fname} {self.lname}, {self.books}\n"