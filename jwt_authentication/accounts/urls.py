from django.urls import path
from .views import UserRegistrationView, UserActivationView

urlpatterns = [
    path(
        route="register/",
        view=UserRegistrationView.as_view(),
        name='user_registration'
    ),
    path(
        route="activate/",
        view=UserActivationView.as_view(),
        name='user_activation'
    )
]