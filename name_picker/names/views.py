from rest_framework.views import APIView
from rest_framework.response import Response
import random


class NamePickerView(APIView):
    """Users can request some names list then return random one name ."""

    def post(self, request, *args, **kwargs):
        requested_names = request.data.get("names", [])
        if requested_names:
            selected_name = random.choice(requested_names)
            return Response({"selected_name": selected_name})
        return Response("Error")
