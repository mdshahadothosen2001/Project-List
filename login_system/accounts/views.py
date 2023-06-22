from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from .templates.accounts.forms import UserForm

def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/register.html',context)
def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html',context)
def homePage(request):
    return render(request, 'accounts/home.html')

