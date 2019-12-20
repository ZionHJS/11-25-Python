from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('login_verify', views.login_verify),
    path('logout', views.logout),
    path('register', views.register),
    path('register_verify', views.register_verify),
    path('clockinout', views.clockinout),
    path('clockinout/get_employee', views.get_employee),
    path('clockin', views.clockin),
    path('clockout', views.clockout),
    path('clockout_lasttime', views.clockout_lasttime),

    path('points', views.points),
    path('report', views.report),
    path('report/report_verify', views.report_verify),
    path('settings', views.settings),
    path('settings/reset_password', views.reset_password_verify),

    path('admin', views.admin),
    path('admin/edit_quote/<int:id>', views.edit_quote),
    path('admin/update_quote/<int:id>', views.update_quote),
    path('admin/award_extra_verify/<int:uid>/<int:cid>', views.award_extra_verify),
    path('admin/edit_employee_verify/<int:id>', views.edit_employee_verify),

    #path('dailyupdates', views.dailyupdates)
]
