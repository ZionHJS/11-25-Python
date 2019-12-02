from django.urls import path
from . import views   

urlpatterns = [
    path('/', views.index),
    path('/new', views.new),
    path('/create', views.new),
    path('/<number>', views.show),
    path('/<number>/delete', views.destroy),
    path('/<number>/edit', views.edit),
    path('/delete/<id>', views.destroy)
]

