from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Used for making custom user"""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=55)
    phone_number = models.IntegerField(max_length=11, unique=True, null=True)
    address = models.CharField(max_length=255)
    profession = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
