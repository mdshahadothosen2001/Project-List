from django.urls import path
from .views import CustomTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="access_token"),
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="refresh_token"),
]
