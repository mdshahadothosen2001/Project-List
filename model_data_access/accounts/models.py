from django.db import models

class persions(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name
