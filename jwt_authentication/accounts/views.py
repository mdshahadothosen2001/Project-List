from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
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

        now_date = datetime.now().date()
        now_time = datetime.now().time().strftime('%H:%M:%S')
        
        otp_obj_date = otp_obj.created_at.date()
        validation_time = timezone.localtime(otp_obj.created_at)+timedelta(minutes=2)
        validation_time  = validation_time.time().strftime('%H:%M:%S')

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