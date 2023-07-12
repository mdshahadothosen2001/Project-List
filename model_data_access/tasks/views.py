from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Tasks

class tasks_view(ListView):
    model = Tasks
#    context_object_name = 'tasks'
#    template_name = 'tasks/tasks_list.html'

class tasks_detail(DetailView):
    model = Tasks
    context_object_name = 'task'

class task_create(CreateView):
    model = Tasks
    template_name = 'tasks/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class task_update(UpdateView):
    model = Tasks
    fields = '__all__'
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('tasks')