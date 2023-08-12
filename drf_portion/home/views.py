from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldView(APIView):
    def get(request, format=None):
        return Response({'message':"Hello Word"})