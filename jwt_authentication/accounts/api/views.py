from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """This class is a custom serializer for obtaining authentication tokens"""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["current_date"] = datetime.now().strftime("%Y:%m:%d")
        current_time = datetime.now().strftime("%I:%M:%p")
        token["current_time"] = current_time
        if "AM" in current_time:
            token["day_status"] = "Day"
        else:
            token["day_status"] = "Night"
        token["location"] = "Dhaka"

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    """User can get access token and refresh token by thier email and password"""

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
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


@api_view(["GET"])
def getRoutes(request):

    routes = ["/api/token/", "/api/token/refresh/", "/api/home/"]
    return Response(routes)


class home_view(APIView):
    """User can loggin with access token"""

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Welcome to the home view!"})
