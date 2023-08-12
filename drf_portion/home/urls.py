from django.urls import path
from .views import hello_world_view


urlpatterns = [
    #http://127.0.0.1:8000/home/hello/
    path(
        route = 'hello/',
        view = hello_world_view,
        name = 'hello'
    ),
]