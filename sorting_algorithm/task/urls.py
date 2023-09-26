from django.urls import path
from .views import HomeView


urlpatterns = [
    #   GET:localhost:8000/
    path(route="", view=HomeView.as_view(), name="home")
]
