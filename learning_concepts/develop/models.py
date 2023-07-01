from django.db import models

class workers(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    