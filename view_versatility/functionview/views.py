from django.shortcuts import render
from django.http import HttpResponse

def home_template_view(request):
    context = "Hello World!"
    return HttpResponse(context)
