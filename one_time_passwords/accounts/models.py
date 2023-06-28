from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number is required!')

        extra_fields['email'] = self.normalize_email(extra_fields.get('email'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
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

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.father_name + ' ' + self.mother_name

    def get_short_name(self):
        return self.father_name

    def __str__(self):
        return self.phone_number
