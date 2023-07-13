from django.db import models

class Car(models.Model):
    model_name = models.CharField(max_length=55)
    year = models.IntegerField()
    driving_id = models.CharField(max_length=55)