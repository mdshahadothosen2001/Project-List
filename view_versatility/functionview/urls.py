from django.urls import path
from .views import home_template_view
urlpatterns = [
    path('',home_template_view, name='home')
]