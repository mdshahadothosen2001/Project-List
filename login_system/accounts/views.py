from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login

from .templates.accounts.forms import UserForm


def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            user = form.cleaned_data.get('username')
            messages.success(request,'Account Created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html',context)
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password incorrect ! please check this')
            
    context = {}
    return render(request, 'accounts/login.html',context)
def homePage(request):
    return render(request, 'accounts/home.html')

