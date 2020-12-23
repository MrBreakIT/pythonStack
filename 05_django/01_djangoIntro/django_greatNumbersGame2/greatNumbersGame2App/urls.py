from django.urls import path     
from . import views



urlpatterns = [
    path("", views.index),
    path("takeGuess", views.takeGuess),
    path("reset", views.reset)
]