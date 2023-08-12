from django.urls import path
from .views import UserListCreateView


urlpatterns = [
    #http://127.0.0.1:8000/accounts/user/
    path(
        route = 'user/', 
        view = UserListCreateView.as_view(),
        name='user_list'),
]