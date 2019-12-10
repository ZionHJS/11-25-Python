from django.conf.urls import url
from . import views

urlpatterns = [
    url('amadon', views.index),
    url('amadon/checkout', views.checkout)
]