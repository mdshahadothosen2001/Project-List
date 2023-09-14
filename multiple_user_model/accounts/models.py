from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.query import QuerySet


class User(AbstractUser):
    """Used for all users like users of admin and student and teacher"""

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.ADMIN

    role = models.CharField(max_length=55, choices=Role.choices)

    def save(self, *args, **kwarg):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwarg)


class AdminManager(BaseUserManager):
    """Used to filter for admin model"""

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.ADMIN)


class Admin(User):
    """Used for create and access those admin user whose role is admin"""

    base_role = User.Role.ADMIN

    admin = AdminManager()

    class Meta:
        proxy = True


class StudentManager(BaseUserManager):
    """Used to filter for student model"""

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.STUDENT)


class Student(User):
    """Used for create and access those student user whose role is student"""

    base_role = User.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True


class TeacherManager(BaseUserManager):
    """Used to filter for teacher model"""

    def get_queryset(self, *args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role=User.Role.TEACHER)


class Teacher(User):
    """Used for create and access those teacher user whose role is teacher"""

    base_role = User.Role.TEACHER

    teacher = TeacherManager()

    class Meta:
        proxy = True
