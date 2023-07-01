from django.shortcuts import render
from django.views.generic.list import ListView
from .models import workers

class worker_list(ListView):
    model = workers
#    template_name = 'worker.worker_list.html'
    context_object_name = 'workers'

def workers_data(request):
    worker = workers.objects.all()
    context = {
        'worker':worker
    }
    return render(request, 'develop/workers_list.html', context)

