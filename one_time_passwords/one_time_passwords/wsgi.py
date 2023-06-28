import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'one_time_passwords.settings')

application = get_wsgi_application()
