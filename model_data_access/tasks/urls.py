from django.urls import path
from .views import tasks_view, tasks_detail, task_create, task_update
urlpatterns = [
    path('tasks/', tasks_view.as_view(), name='tasks'),
    path('tasks/task/<int:pk>', tasks_detail.as_view(), name='task'),
    path('create/', task_create.as_view(), name='task-create'),
    path('update/<int:pk>', task_update.as_view(), name='task-update')
]