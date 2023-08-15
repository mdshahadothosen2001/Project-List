from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


class CustomUserModel(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=11, unique=True)
    father_name = models.CharField(max_length=55)
    mother_name = models.CharField(max_length=55)
    brother_name = models.CharField(max_length=55)
    sister_name = models.CharField(max_length=55)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    religion = models.CharField(max_length=20)
    nationality = models.CharField(max_length=55)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    objects = UserManager()
