from django.urls import path
from .views import message_display, home_view, home_with_get_method

urlpatterns = [
    path("", message_display.as_view(), name="message"),
    path("home_get", home_with_get_method.as_view(), name="home_get"),
    path("home", home_view.as_view(), name="home"),
]
