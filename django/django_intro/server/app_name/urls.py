from django.urls import path
from . import views   

urlpatterns = [
    #path('<str:name>', views.index),   #how to pass multiple parameters

    path('', views.empty),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show),
    path('<int:number>/delete', views.destroy),
    path('<int:number>/edit', views.edit),
    path('<int:number>/delete', views.destroy),
]

