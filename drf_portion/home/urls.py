from django.urls import path
from .views import HelloWorldView


urlpatterns = [
    #http://127.0.0.1:8000/home/hello/
    path(
        route = 'hello/',
        view = HelloWorldView,
        name = 'hello'
    ),
]