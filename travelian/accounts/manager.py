from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    "Used to help user instance"

    def create_user(self, email, password=None, **extra_field):
        "used fo create user account"

        if not email:
            return ValueError("Required email")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_field):
        """Used to create super user"""

        extra_field.setdefault("is_active", True)
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_field)
