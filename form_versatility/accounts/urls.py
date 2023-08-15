from django.urls import path
from .views import car_form, car_list, car_form_fields, car_form_default

urlpatterns = [
    path("car-form/", car_form, name="car_form"),
    path("cars/", car_list.as_view(), name="cars"),
    path("car-form-fields/", car_form_fields, name="car_form_fields"),
    path("car_form_default/", car_form_default.as_view(), name="car_form_default"),
]
