from django.urls import path
from .views import UserRegistrationView, User_Registration_View

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('registers/', User_Registration_View.as_view(), name='registers'),
]