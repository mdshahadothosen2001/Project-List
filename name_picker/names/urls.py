from django.urls import path
from .views import NamePickerView, home_view

urlpatterns = [
    # GET: http://127.0.0.1:8000/
    path(route="", view=home_view.as_view(), name="home"),
    # POST: http://127.0.0.1:8000/name-picker/
    path(route="name-picker/", view=NamePickerView.as_view(), name="pick_name"),
]
