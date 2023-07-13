from django.urls import path
from .views import car_form, car_list
urlpatterns = [
    path('car-form/', car_form, name='car_form'),
    path('cars/', car_list.as_view(), name='cars')
]