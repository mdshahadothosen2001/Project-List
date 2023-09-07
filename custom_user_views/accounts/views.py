from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .templates.accounts.forms import UserForm
from .redicoretors import unauthenticated_user, allowed_users


@unauthenticated_user
def registerPage(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            default_group = Group.objects.get(name="customer")
            user.groups.add(default_group)

            messages.success(request, "Account Created for " + user.username)
            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password incorrect ! please check this")

    context = {}
    return render(request, "accounts/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin", "customer"])
def homePage(request):
    user = request.user.groups.get()
    context = {"user": user}
    return render(request, "accounts/home.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin", "customer"])
def create_item(request):
    return render(request, "items/item.html")
