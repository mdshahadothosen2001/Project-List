import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one_time_passwords.settings')

application = get_asgi_application()
