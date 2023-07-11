from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.name