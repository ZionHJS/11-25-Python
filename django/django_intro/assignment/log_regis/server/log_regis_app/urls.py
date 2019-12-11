from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.regisration),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('post_post', views.post_post),
    path('post_comment/<int:id>', views.post_comment)
]

