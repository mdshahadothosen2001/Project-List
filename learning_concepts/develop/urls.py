from django.urls import path
from .views import worker_list
urlpatterns=[
    path('workers/', worker_list.as_view(), name='workers'),
]
