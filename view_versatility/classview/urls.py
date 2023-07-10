from django.urls import path
from .views import message_display, home_view
urlpatterns = [
    path('',message_display.as_view(), name='message'), 
    path('home',home_view.as_view(), name='home'),
]