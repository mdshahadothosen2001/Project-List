from django.urls import path
from .views import ProductListView, ProductOrderView, home_view


urlpatterns = [
    # GET: http://127.0.0.1:8000/base/home/
    path(route="home/", view=home_view.as_view(), name="home"),
    # GET: http://127.0.0.1:8000/base/
    path(route="", view=ProductListView.as_view(), name="products"),
    # POST: http://127.0.0.1:8000/base/order
    path(route="order/", view=ProductOrderView.as_view(), name="order"),
]
