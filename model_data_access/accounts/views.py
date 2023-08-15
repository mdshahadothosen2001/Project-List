from django.shortcuts import render
from django.views.generic import ListView
from .models import persions


def data_view(request):
    persion = persions.objects.all()
    context = {"persions": persion}
    return render(request, "accounts/data_view.html", context)


class data_display_view(ListView):
    model = persions


#    template_name = 'accounts/persions_list.html'
#    context_object_name = 'persions'
