from django.conf import settings
import jwt


def token_validation(request):
    token = request.session.get('token')
    if token:
        secret_key = settings.SECRET_KEY
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload