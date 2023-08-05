from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import UserRegistrationSerializer
from .otp_send import send_otp_to_email
from .models import CustomUser
from .models import OTP


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""
    
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs): 
        email = request.data.get('email')   
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        
        if first_name is None or last_name is None:
            raise ValidationError('you can not create user without fulfill name fields!')
        
        otp = send_otp_to_email(email)
        OTP.objects.create(email=email, otp=otp)

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

class UserActivationView(APIView):
    """User can activate account by OTP received through email."""
    
    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            raise ValidationError('Please provide both email and OTP.')

        otp_obj = get_object_or_404(OTP,email=email, otp=otp)

        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        otp_obj.delete()

        return Response('Your account has been activated!')