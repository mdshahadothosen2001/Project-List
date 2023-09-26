from django.db import models


class task(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        """scpecific tell to django model how does behavior and descending ordering"""

        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = "task"
        ordering = ["-created_at"]
