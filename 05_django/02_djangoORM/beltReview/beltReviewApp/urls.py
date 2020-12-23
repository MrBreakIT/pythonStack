from django.urls import path, include
from . import views

urlpatterns = [
    #***********************************
    #           Index
    path('', views.index),
    path("login", views.login),    
    path("home", views.home),
    path("registerUser", views.registerUser),
    # path("register", views.register),
    path("logout", views.logout),

    #***********************************
    #        Books Homepage 
    path("addBook_Review", views.addBook_Review),
    path("createBook_Review", views.createBook_Review),





]