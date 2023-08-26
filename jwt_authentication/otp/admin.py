from django.contrib import admin
from .models import OTP


class AuthenticationAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")


admin.site.register(OTP)
