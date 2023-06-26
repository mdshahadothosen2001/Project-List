import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'custom_user_views.settings')

application = get_asgi_application()
