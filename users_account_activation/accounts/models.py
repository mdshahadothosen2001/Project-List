from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class custom_users(AbstractUser):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    phone_number = models.IntegerField(unique=True, blank=True, null=True)
    brother_name = models.CharField(max_length=55)
    sister_name = models.CharField(max_length=55)
    age = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=55)
    religion = models.CharField(max_length=55)
    nationality = models.CharField(max_length=55)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
