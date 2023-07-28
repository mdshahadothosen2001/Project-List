import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_account_activation.settings')

application = get_wsgi_application()
