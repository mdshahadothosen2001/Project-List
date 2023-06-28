from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if len(form.cleaned_data.get('phone_number'))==11:
                    form.save()
                    user = form.cleaned_data.get('phone_number')
                    messages.success(request, 'Account created for ' + user)
                    return redirect('login')
                else:
                    messages.info(request,'required phone number exact 11 digit!')
                    return redirect('register')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password incorrect ! double check please')
            
        context = {}
        return render(request, 'accounts/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def homePage(request):
    return render(request, 'accounts/home.html')

