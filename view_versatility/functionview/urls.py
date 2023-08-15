from django.urls import path
from .views import message_view, home_template_view

urlpatterns = [
    path("", message_view, name="home"),
    path("home/", home_template_view, name="home"),
]
