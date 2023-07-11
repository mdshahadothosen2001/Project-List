from django.urls import path
from .views import data_view
urlpatterns = [
    path('data-view/', data_view, name='data-view'),
]