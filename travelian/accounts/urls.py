from django.urls import path
from .views import CustomTokenObtainPairView, HomeView

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # GET: http://127.0.0.1:8000/
    path(route="", view=HomeView.as_view(), name="home"),
    # POST: http://127.0.0.1:8000/token/
    path(route="token/", view=CustomTokenObtainPairView.as_view(), name="access_token"),
    # POST: http://127.0.0.1:8000/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="refresh_token"),
]
