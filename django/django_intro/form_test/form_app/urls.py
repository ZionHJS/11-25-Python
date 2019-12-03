from django.urls import path
from . import views

urlpartterns = [
    path('', views.index),
    path('users', views.create_user)
]


