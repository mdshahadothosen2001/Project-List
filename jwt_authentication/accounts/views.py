from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError

from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    """ A class-based view for user regitration by json request api.
    This view api need permission to authentication any authenticated user.
    This class firstly check first name and last name included in request api to create user, 
    if True then return validation error message.

    Called UserRegistrationSerializer and check is valid or not,
    If valid then save data and return successfull message.

    Usage:
    . Make a POST request to this view with fields in the request body.
    . If fields is empy or missing any field,
      it will return validation error message 'you can not create user without fulfill name fields!'.
    . If serializer data is valid, 
      it will return successfull message 'succesfull! user is created'.

    # Resuest:
    POST /api-auth/register/


    """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs): 
        email = request.data.get('email')   
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        if first_name is None or last_name is None:
            raise ValidationError('you can not create user without fulfill name fields!')

        user_info = {
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":password
        }
        serializer = UserRegistrationSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            return Response('succesfull! user is created')
