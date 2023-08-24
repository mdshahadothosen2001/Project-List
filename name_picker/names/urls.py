from django.urls import path
from .views import NamePickerView

urlpatterns = [
    # http://127.0.0.1:8000/names/
    path(route="", view=NamePickerView.as_view(), name="pick_name"),
]
