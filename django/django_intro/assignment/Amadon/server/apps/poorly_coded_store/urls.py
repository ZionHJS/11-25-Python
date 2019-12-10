from django.urls import path
from . import views

urlpatterns = [
    path('amadon', views.index),
    path('amadon/checkout', views.checkout),
    path('amadon/checkout/thankyou<dic:context>', views.thankyou),
]
