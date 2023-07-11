from django.urls import path
from .views import tasks_view, tasks_detail
urlpatterns = [
    path('tasks/', tasks_view.as_view(), name='tasks'),
    path('tasks/task/<int:pk>', tasks_detail.as_view(), name='task'),
]