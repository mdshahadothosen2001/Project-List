from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


from datetime import datetime, timedelta
import pyotp
from .models import CustomUser

from .forms import RegistrationForm
from .otp import sent_otp


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                if len(form.cleaned_data.get("phone_number")) == 11:
                    form.save()
                    user = form.cleaned_data.get("phone_number")
                    messages.success(request, "Account created for " + user)
                    return redirect("login")
                else:
                    messages.info(request, "required phone number exact 11 digit!")
                    return redirect("register")

        context = {"form": form}
        return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                sent_otp(request)
                request.session["username"] = username
                return redirect("otp")
            else:
                messages.info(
                    request, "Username or Password incorrect ! double check please"
                )

        context = {}
        return render(request, "accounts/login.html", context)


def otp_validation(request):
    if request.method == "POST":
        otp = request.POST["otp"]
        username = request.session["username"]

        otp_secret_key = request.session["otp_secret_key"]
        otp_valid_until = request.session["otp_valid_date"]

        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)

                if totp.verify(otp):
                    user = get_object_or_404(CustomUser, phone_number=username)
                    login(request, user)

                    del request.session["otp_secret_key"]
                    del request.session["otp_valid_date"]

                    return redirect("home")
                else:
                    pass
            else:
                pass

        else:
            pass

    else:
        pass
    return render(request, "validations/otp.html")


def logoutPage(request):
    logout(request)
    return redirect("login")


def logoutPage(request):
    logout(request)
    return redirect("login")


def homePage(request):
    return render(request, "accounts/home.html")
