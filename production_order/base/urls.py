from django.urls import path
from .views import ProductListView, ProductOrderConfirmView

urlpatterns = [
    # http://127.0.0.1:8000/
    path(route="", view=ProductListView.as_view(), name="products"),
    # http://127.0.0.1:8000/product/<int:pk>/
    path(
        route="product/<int:pk>/",
        view=ProductOrderConfirmView.as_view(),
        name="product",
    ),
]
