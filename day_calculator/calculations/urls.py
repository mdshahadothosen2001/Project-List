from django.urls import path
from .views import DateCalculationView


urlpatterns = [
    # POST: http://127.0.0.1:8000
    path(route="", view=DateCalculationView.as_view(), name="days"),
]
