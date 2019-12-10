from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regisration),
    path('success', views.success),
    path('logout', views.logout, name='logout'),
]

