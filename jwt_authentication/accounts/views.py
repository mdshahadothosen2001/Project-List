from django.shortcuts import get_object_or_404
from datetime import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import UserRegistrationSerializer
from .otp_send import otp_send
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

        user_info = {
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":password
        }
        serializer = UserRegistrationSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            otp_send(email)
            return Response('succesfull! user is created')

class UserActivationView(APIView):
    """User can activate account by OTP received through email."""
    
    def patch(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            raise ValidationError('Please provide both email and OTP.')

        otp_obj = get_object_or_404(OTP,email=email, otp=otp)

        now = datetime.now()
        now_date = f"{now.day:02d}:{now.month:02d}:{now.year}"
        now_time = (now.hour*3600)+ (now.minute*60)+ (now.second)
        
        created_time = otp_obj.created_at
        created_time = timezone.localtime(created_time)
        otp_obj_date = f"{created_time.day:02d}:{created_time.month:02d}:{created_time.year}"
        otp_obj_time = (created_time.hour*3600)+ (created_time.minute*60)+ (created_time.second)
        validation_time = otp_obj_time+(120)

        if now_date != otp_obj_date:
            otp_obj.delete()
            return Response('Timeout!, OTP has expired.')
        if now_time >= validation_time:
            otp_obj.delete()
            return Response('Timeout!, OTP has expired.')
        
        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        otp_obj.delete()
        return Response('Your account has been activated!')