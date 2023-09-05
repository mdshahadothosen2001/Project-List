from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from product.models import Product
from order.models import Order


class ProductListView(ListView):
    """Display product list"""

    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"
    success_url = reverse_lazy("products")


class ProductOrderConfirmView(LoginRequiredMixin, DetailView):
    """User can Order from product table"""

    model = Product
    template_name = "product/product_order.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        """Select product for order"""

        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:

            selected_product = context["product"]
            if selected_product:
                order = Order.objects.create(user=self.request.user)
                order.products.add(selected_product)
                order.save()
                context["message"] = "order confirmed"
        return context
