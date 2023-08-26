from django.urls import path
from .views import getRoutes
from .views import MyTokenObtainPairView, home_view

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    # GET: localhost:8000/
    path("", getRoutes),
    # POST: localhost:8000/api/token/
    path(
        route="token/", view=MyTokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    # localhost:8000/api/token/refresh/
    path(route="token/refresh/", view=TokenRefreshView.as_view(), name="token_refresh"),
    # GET: localhost:8000/api/home/
    path(route="home/", view=home_view.as_view(), name="home"),
]
