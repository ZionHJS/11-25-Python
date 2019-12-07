from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows/create_show', views.create_show),
    path('shows/<int:id>', views.show_this_show),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/edit/update', views.edit_show_update),
    path('shows/<int:id>/delete', views.delete_show),
]
