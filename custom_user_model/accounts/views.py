from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registerPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def homePage(request):
    return render(request, 'accounts/home.html')
