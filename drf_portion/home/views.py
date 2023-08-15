from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldView(APIView):
    def patch(self, request, format=None):
        print(request.data)
        print("method name ", request.method)
        return Response({"message": "Hello Word", "user_data": request.data})
