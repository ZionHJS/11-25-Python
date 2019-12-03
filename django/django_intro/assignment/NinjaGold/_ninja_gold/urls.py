from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('process_farm', views.process_farm),
    path('process_cave', views.process_cave),
    path('process_house', views.process_house),
    path('process_casino', views.process_casino)
]

