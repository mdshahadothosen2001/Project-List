import random
from django.core.mail import send_mail
from django.conf import settings
from .models import OTP


def send_otp_to_email(email):
    otp = random.randint(1000,9999)
    try:
        subject = 'Your OTP for registration'
        message = f'Your OTP is: {otp}'
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [email])
        print(f"{otp} OTP successfully sent to {email}")
        return otp
    except Exception as e:
        print("Error sending OTP :",e)

def otp_send(email):
    otp = send_otp_to_email(email)
    try:
        otp_instance = OTP.objects.get(email=email)
        otp_instance.otp = otp
        otp_instance.save()
    except OTP.DoesNotExist:
        otp_instance = OTP.objects.create(email=email, otp=otp)