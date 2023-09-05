from django.urls import path
from .views import ProductListView

urlpatterns = [
    # http://127.0.0.1:8000/
    path(route="", view=ProductListView.as_view(), name="create_order"),
]
