from django.urls import path
from .views import worker_list, workers_data
urlpatterns=[
    path('workers/', worker_list.as_view(), name='workers'),
    path('workers-data/', workers_data, name='workers-data'),
]
