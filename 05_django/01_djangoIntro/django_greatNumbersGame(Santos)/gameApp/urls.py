from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path("guess", views.guess),
    path("reset", views.reset)
]