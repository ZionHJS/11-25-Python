from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.regisration),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('books/add', views.add),
]
