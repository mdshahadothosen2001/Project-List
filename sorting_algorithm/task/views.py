from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    """used for display success message"""

    def get(self, *args, **kwargs):
        payload = {"message": {"code": 200, "status": "True", "dir": "home"}}

        return Response(payload)
