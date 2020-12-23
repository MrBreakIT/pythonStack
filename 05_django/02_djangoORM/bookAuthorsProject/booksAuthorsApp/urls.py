from django.urls import path, include
from . import views


urlpatterns = [
    #***********************************
    #           Landing Page
    path('', views.index),
    path("login", views.login),    
    path("home", views.home),
    path("registerUser", views.registerUser),
    path("register", views.register),
    path("logout", views.logout),
    

    #***********************************
    #           Books
    #    
    path("booksHomepage", views.booksHomepage),
    path("createBook", views.createBook),
    path("books/<int:titleID>", views.showTitle),
    path("addAuthor/<int:bookinfo>", views.addAuthor),
    path("delete/<int:titleID>", views.deleteBook),
    path("edit/<int:titleID>", views.editBook),
    path("updateBook/<int:titleID>", views.updateBook),
    #************************************
    #           Authors
    #
    path("authorsHomepage", views.authorsHomepage),
    path("createAuthor", views.createAuthor),
    path("author/<int:authorID>", views.showAuthor),
    path("addBookToAuthor/<int:authorID>", views.addBookToAuthor),
    path("deleteAuthor/<int:authorID>", views.deleteAuthor),
    path("editAuthor/<int:authorID>", views.editAuthorpage),
    path("updateAuthor/<int:authorID>", views.updateAuthor),
]











