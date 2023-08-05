from django.urls import path
from .views import UserRegistrationView, UserActivation

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('activate/', UserActivation.as_view(), name='activate'),
]