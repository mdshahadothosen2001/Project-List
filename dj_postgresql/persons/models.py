from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=105, null=True)
    age = models.IntegerField(default=None, null=True, blank=True)
    address = models.CharField(max_length=205, null=True)
