import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""
    
    permission_classes = [AllowAny]

    def generate_otp(self):
        return ''.join(random.choices(string.digits, k=6))
    
    def send_otp_email(self, email, otp):
        print(f"Sending OTP: {otp} to {email}")

    def post(self, request, *args, **kwargs): 
        email = request.data.get('email')   
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        if first_name is None or last_name is None:
            raise ValidationError('you can not create user without fulfill name fields!')
                          
        otp = self.generate_otp()
        self.send_otp_email(email, otp)
        
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
