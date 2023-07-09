from django.urls import path
from .views import message_display
urlpatterns = [
    path('',message_display.as_view(), name='message'),
]