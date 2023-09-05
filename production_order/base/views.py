from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from product.models import Product


class ProductListView(ListView):
    """Display product list"""

    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """User can Order from product table"""

    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"
