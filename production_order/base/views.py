from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from product.models import Product
from order.models import Order


class ProductListView(ListView):
    """Display product list"""

    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"
