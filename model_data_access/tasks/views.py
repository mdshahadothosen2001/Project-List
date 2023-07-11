from django.views.generic import ListView, DetailView

from .models import Tasks

class tasks_view(ListView):
    model = Tasks
#    context_object_name = 'tasks'
#    template_name = 'tasks/tasks_list.html'

class tasks_detail(DetailView):
    model = Tasks
    context_object_name = 'task'
