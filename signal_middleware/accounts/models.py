from django.db import models

class User(models.Model):
    email = models.CharField(max_length=55)
    name = models.CharField(max_length=55)
    city = models.CharField(max_length=55)

    def __str__(self):
        return self.email