from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from .serializers import UserRegistrationSerializer
from otp.otp_send import otp_send
from .models import CustomUser
from otp.models import OTP
from .utils import token_validation
from .utils import recovery_key


class UserRegistrationView(APIView):
    """Users can register their account by email, frist_name, last_name and password."""

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        """Used to create user account and send otp by calling otp function"""

        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        password = request.data.get("password")

        if first_name is None or last_name is None:
            raise ValidationError(
                "you can not create user without fulfill name fields!"
            )

        user_info = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
        }

        serializer = UserRegistrationSerializer(data=user_info)
        if serializer.is_valid():
            serializer.save()
            otp_send(email)

            return Response("succesfull! user is created")


class UserActivationView(APIView):
    """User can activate account by OTP received through email."""

    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        """Used to update user activate status by otp confirm"""

        email = request.data.get("email")
        otp = request.data.get("otp")

        if not email or not otp:
            raise ValidationError("Please provide both email and OTP.")

        otp_obj = get_object_or_404(OTP, email=email, otp=otp)

        now_date = datetime.now().date()
        now_time = datetime.now().time().strftime("%H:%M:%S")

        otp_obj_date = otp_obj.created_at.date()
        validation_time = timezone.localtime(otp_obj.created_at) + timedelta(minutes=2)
        validation_time = validation_time.time().strftime("%H:%M:%S")

        if now_date != otp_obj_date:
            otp_obj.delete()

            return Response("Timeout!, OTP has expired.")

        if now_time >= validation_time:
            otp_obj.delete()

            return Response("Timeout!, OTP has expired.")

        user = CustomUser.objects.get(email=email)
        user.is_active = True
        user.save()
        otp_obj.delete()

        return Response("Your account has been activated!")


class UserPasswordResetView(APIView):
    """User can change thier password by token with new password"""

    permission_classes = [AllowAny]

    def patch(self, request, *args, **kwargs):
        """This method used to recreate user password when user logined"""

        new_password = request.data.get("new_password")

        if not new_password:
            raise ValidationError("new_password required")

        payload = token_validation(request)
        email = payload.get("email")

        if email:
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password)
            user.save()

            return Response({"message": "successfully changed password"})

        else:
            return Response("Email not found!")


class ForgottenPasswordResetView(APIView):
    """User can recreate password by thier email and first_name"""

    def patch(self, request):
        """This method used to generate temporary password"""

        email = request.data.get("email")
        first_name = request.data.get("first_name")

        if email and first_name:
            recovery_password = recovery_key(email)
            user = get_object_or_404(CustomUser, email=email, first_name=first_name)
            user.set_password(recovery_password)
            user.save()

            return Response("successfully done!")

        raise ValidationError("Required email and name first name")
