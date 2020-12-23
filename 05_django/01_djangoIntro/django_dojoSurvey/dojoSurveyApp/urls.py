from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.result),
    # path('success', views.success)
]





