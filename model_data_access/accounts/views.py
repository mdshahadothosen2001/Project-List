from django.shortcuts import render
from .models import persions

def data_view(request):
    persion = persions.objects.all()
    context = {
        'persions' : persion
    }
    return render(request, 'accounts/data_view.html', context)
