from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import random


class NamePickerView(APIView):
    """Users can request some names list then return random one name ."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        requested_names = request.data.get("names", [])

        if requested_names:
            selected_name = random.choice(requested_names)

            return Response({"selected_name": selected_name})

        return Response("Error")


class home_view(APIView):
    """User can loggin with access token"""

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Used for return successful message"""

        return Response({"message": "Welcome to the home view !"})
