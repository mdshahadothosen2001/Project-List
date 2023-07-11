from django.views.generic import ListView

from .models import Tasks

class tasks_view(ListView):
    model = Tasks
#    context_object_name = 'tasks'
#    template_name = 'tasks/tasks_list.html'
