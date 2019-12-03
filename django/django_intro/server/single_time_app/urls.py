from django.urls import path
from . import views   

urlpatterns = [
    #path('<str:name>', views.index),   #how to pass multiple parameters
    path('', views.showTime),
]

