from django.contrib import admin
from .models import task


class TaskAdmin(admin.ModelAdmin):
    """custom interface at admin panel"""

    list_display = (
        "id",
        "title",
        "description",
    )
    list_display_links = ("title",)
    search_fields = ("title",)


admin.site.register(task, TaskAdmin)
