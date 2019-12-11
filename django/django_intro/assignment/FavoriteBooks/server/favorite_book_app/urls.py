from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regisration),
    path('login', views.login),
    path('books', views.books),
    path('add_book', views.add_book),
]