from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add2', views.add2),
    path('yourChoice', views.yourChoice),
    path('destroySession', views.destroySession),
]


























