from django.urls import path
from .views import NamePickerView, home_view

urlpatterns = [
    # POST: http://127.0.0.1:8000/names/
    path(route="picker/", view=NamePickerView.as_view(), name="pick_name"),
    # GET: http://127.0.0.1:8000/names/home/
    path(route="", view=home_view.as_view(), name="home"),
]
