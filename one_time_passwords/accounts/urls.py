from django.urls import path
from .views import homePage , registerPage , loginPage , logoutPage

urlpatterns=[
    path('register/',registerPage,name='register'),
    path('',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('home/',homePage,name='home'),
]