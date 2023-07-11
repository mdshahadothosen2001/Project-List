from django.urls import path
from .views import data_view, data_display_view
urlpatterns = [
    path('data-view/', data_view, name='data-view'),
    path('data/', data_display_view.as_view(), name='data'),
]