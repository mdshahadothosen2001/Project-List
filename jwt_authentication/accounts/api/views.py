from rest_framework.response import Response
from rest_framework.decorators import api_view 


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['current_time'] = datetime.now().strftime('%Y:%m:%d')
        current_time = datetime.now().strftime('%I:%M:%p')

        if 'AM' in current_time:
            token['Day_status'] = 'Day'
        else:
            token['Day_status'] = 'Night'

        token['current_date'] = current_time
        token['location'] = 'Dhaka'
        

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)