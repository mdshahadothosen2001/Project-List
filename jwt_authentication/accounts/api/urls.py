from django.urls import path
from .views import getRoutes
from .views import MyTokenObtainPairView, home_view

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('',getRoutes),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', home_view.as_view(), name='home'),
]