from django.shortcuts import render
from django.http import HttpResponse

def message_view(request):
    context = "Hello World!"
    return HttpResponse(context)

def home_template_view(request):
    context = {
        'message':"Hello World!"
    }
    return render(request, 'functionview/home.html', context)
