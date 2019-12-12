from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.regisration),
    path('login', views.login),
    path('logout', views.logout),
    path('books', views.books),
    path('books/add', views.add),
    path('books/add_validate', views.add_validate),
    path('books/<int:id>', views.show_cur_book),
    path('books/<int:id>/add_review', views.book_add_review),
    path('users/<int:id>', views.show_cur_user),
    path('delete_review/<int:bid>/<int:rid>', views.delete_review)
]
