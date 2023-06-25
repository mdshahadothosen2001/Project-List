from django.urls import path
from .views import homePage, registerPage

urlpatterns=[
    path('register/',registerPage,name='register'),
    path('',homePage,name='home'),
]