from django.urls import path, include

urlpatterns = [
    path('', include('form_app.urls')),
]
