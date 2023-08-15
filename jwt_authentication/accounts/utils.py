from django.conf import settings
from django.core.mail import send_mail
import jwt
import random
import string


def token_validation(request):
    token = request.session.get("token")
    if token:
        secret_key = settings.SECRET_KEY
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload


def recovery_key(email):
    recovery_password = generate_random_string(9)
    subject = "Your recovery password"
    message = f"Your recovery password is {recovery_password}. You can login by this key then you should change your password after login."
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [from_email])
    return recovery_password


def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choice(characters) for i in range(length))
    return random_string
