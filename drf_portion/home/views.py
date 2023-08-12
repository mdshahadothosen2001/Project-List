from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def HelloWorldView(request):
    if request.method == 'GET':
        return Response({'message':"this is get method"})
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})