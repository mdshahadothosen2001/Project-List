from django.db import models


class Event(models.Model):
    epic_id = models.IntegerField()
    details = models.TextField()
    years_ago = models.IntegerField()
