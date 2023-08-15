from django.contrib import admin
from .models import country, user_address, address


admin.site.register(country)
admin.site.register(user_address)
admin.site.register(address)
