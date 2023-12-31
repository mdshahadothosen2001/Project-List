from django.urls import path, include
from .views import (
    UserRegistrationView,
    UserActivationView,
    UserPasswordResetView,
    ForgottenPasswordResetView,
)


urlpatterns = [
    # POST: localhost:8000/api-auth/register/
    path(
        route="register/", view=UserRegistrationView.as_view(), name="user_registration"
    ),
    # PATCH: localhost:8000/api-auth/activate/
    path(route="activate/", view=UserActivationView.as_view(), name="user_activation"),
    # PATCH: localhost:8000/api-auth/reset/
    path(route="reset/", view=UserPasswordResetView.as_view(), name="change_password"),
    # PATCH: localhost:8000/api-auth/recover/
    path(
        route="recover/",
        view=ForgottenPasswordResetView.as_view(),
        name="forgotten_password",
    ),
    path("", include("accounts.api.urls")),
]
