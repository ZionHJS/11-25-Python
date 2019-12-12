from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('logoff', views.logoff),
    path('regisration', views.regisration),
    path('register', views.register),
    path('dashboard', views.dashboard)
]