from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regisration),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('books/unfavorite/<int:id>', views.unfavorite),
    path('books/addfavorite/<int:id>', views.addfavorite),
    path('add_book', views.add_book),
    path('books/<int:id>', views.show_book),
    path('update_delete/<int:id>', views.update_delete)
]