from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_verify', views.register_verify),
    path('login_verify', views.login_verify),
    path('wishes', views.wishes),
]
