from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows/new', views.shows_new),
    path('shows/<int:id>', views.shows_new),
    path('shows/<int:id>/edit', views.edit_tvshow),
    path('shows/<int:id>/delete', views.delete_tvshow),
]
