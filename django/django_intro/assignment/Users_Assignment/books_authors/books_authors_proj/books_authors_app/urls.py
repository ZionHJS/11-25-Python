from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_book),
    path('add_book', views.add_book),
    path('books/<int:id>', views.show_book),
    path('books/<int:id>/add_author2book', views.add_author2book),
    path('authors', views.index_author),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.show_author),
    path('authors/<int:id>/add_book2author', views.add_book2author),
]


