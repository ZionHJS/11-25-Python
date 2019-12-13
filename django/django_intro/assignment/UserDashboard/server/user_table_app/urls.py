from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('logoff', views.logoff),
    path('regisration', views.regisration),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('users/edit', views.edit_self),
    path('users/show/<int:id>', views.show_user),
    path('users/show/<int:id>/leave_message', views.leave_message),
    path('user/show/<int:id>/leave_comment/<int:id>', views.leave_comment),
    path('update_info', views.update_info),
    path('update_password', views.update_password),
    path('update_des', views.update_des)
]