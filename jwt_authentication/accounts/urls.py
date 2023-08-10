from django.urls import path
from .views import UserRegistrationView, UserActivationView, UserPasswordResetView, ForgottenPasswordResetView

urlpatterns = [
#localhost:8000/api-auth/register/
    path(
        route="register/",
        view=UserRegistrationView.as_view(),
        name='user_registration'
    ),
#localhost:8000/api-auth/activate/
    path(
        route="activate/",
        view=UserActivationView.as_view(),
        name='user_activation'
    ),
#localhost:8000/api-auth/reset/
    path(
        route="reset/",
        view=UserPasswordResetView.as_view(),
        name='change_password'
    ),
    #localhost:8000/api-auth/recover/
    path(
        route="recover/",
        view=ForgottenPasswordResetView.as_view(),
        name='forgotten_password'
    ),
]