from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('login_verify', views.login_verify),
    path('register', views.register)
]
