from django.conf import settings
import jwt


def get_access_token_from_session(request):
    token = request.session.get('token')
    if token:
        secret_key = settings.SECRET_KEY
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        email = decoded_token.get('email')
        return email