from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldView(APIView):
    def put(self,request, format=None):
        print(request.data)
        return Response({'message':"Hello Word", 'user_data':request.data})