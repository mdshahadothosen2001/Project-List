from django.urls import path
from .views import UserRegistrationView, UserActivationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/', UserActivationView.as_view(), name='activate'),
]