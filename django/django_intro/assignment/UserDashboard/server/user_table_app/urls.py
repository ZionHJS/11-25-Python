from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signin', views.signin),
    path('logoff', views.logoff),
    path('regisration', views.regisration),
    path('register', views.register),
    path('signin_verify', views.signin_verify),
    path('dashboard', views.dashboard),
    path('users/new', views.add_new),
    path('add_new_verify', views.add_new_verify),
    path('users/edit/<int:id>', views.admin_edit_user),
    path('users/remove/<int:id>', views.admin_remove_user),
    path('users/edit', views.edit_self),
    path('users/show/<int:id>', views.show_user),
    path('users/show/<int:id>/leave_message', views.leave_message),
    path('users/show/<int:uid>/leave_comment/<int:mid>', views.leave_comment),
    path('update_info', views.update_info),
    path('update_password', views.update_password),
    path('update_des', views.update_des),
    path('admin_update_info/<int:id>', views.admin_update_info),
    path('admin_update_password/<int:id>', views.admin_update_password)
]
