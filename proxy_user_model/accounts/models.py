from django.db import models
from django.contrib.auth.models import User


class Student(User):
    class Meta:
        ordering = ("first_name",)

        proxy = True


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(first_name="teacher")


class Teacher(User):
    class Meta:
        ordering = ("first_name",)

        proxy = True

    objects = TeacherManager()
