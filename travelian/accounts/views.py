from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serilizers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """User can get access token and refresh token by thier email and password"""

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """Used to return access token and refresh token"""

        response = super().post(request, *args, **kwargs)
        access_token = str(response.data["access"])
        refresh_token = str(response.data["refresh"])

        token_data = {
            "access": access_token,
            "refresh": refresh_token,
        }

        token = access_token
        request.session["token"] = token

        return Response(token_data)


class HomeView(APIView):
    """Used for authenticated by token"""

    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        """Used for response success message"""

        return Response({"message": "you are authenticated"})
