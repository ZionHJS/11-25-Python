from django.urls import path
from . import views   

urlpatterns = [
    path('/new', views.new),
    path('/create', views.new),
    path('/<number>'),
    path('/<number>/delete', views.delete),
    path('/delete/<id>')
]
