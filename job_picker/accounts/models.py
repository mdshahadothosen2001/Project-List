from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    designation = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=55)
    contact_info = models.IntegerField()
    skills = models.CharField(max_length=555)
    experience = models.IntegerField(null=True)
    social_link = models.CharField(max_length=255)
    projects = models.CharField(max_length=555)
    achievements = models.CharField(max_length=555)
    extracurricular_activities = models.CharField(max_length=555)
    interest = models.CharField(max_length=555)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "contact_info"]
