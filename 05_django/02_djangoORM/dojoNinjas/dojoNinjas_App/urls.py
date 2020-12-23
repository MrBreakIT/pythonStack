from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addDojo', views.addDojo),
    path('addNinja', views.addNinja),
    path('deleteDojo', views.deleteDojo)
]




