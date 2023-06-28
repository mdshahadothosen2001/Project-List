from django.urls import path
from .views import homePage , registerPage , loginPage , logoutPage, otp_validation

urlpatterns=[
    path('register/',registerPage,name='register'),
    path('',loginPage,name='login'),
    path('otp', otp_validation, name='otp'),
    path('logout/',logoutPage,name='logout'),
    path('home/',homePage,name='home'),
]