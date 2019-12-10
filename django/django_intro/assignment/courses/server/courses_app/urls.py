from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course', views.add_course),
    path('show_remove/<int:id>', views.show_remove),
    path('real_remove/<int:id>', views.remove)
]
