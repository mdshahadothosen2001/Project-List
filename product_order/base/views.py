from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from product.models import Product
from order.models import Order


class ProductListView(APIView):
    """Users can see the product list."""

    def get(self, request, *args, **kwargs):
        """Used for return product details."""

        product_queryset = Product.objects.all()
        serializer = ProductSerializer(product_queryset, many=True)

        return Response({"products": serializer.data})


class ProductOrderView(APIView):
    """Users can order selected from the product list."""

    def post(self, request, *args, **kwargs):
        """Used to get data from user."""

        selected_products = request.data.get("products")
        user = request.user

        if not selected_products:
            raise ValidationError("product required")

        if user.is_authenticated:

            new_order = Order()
            new_order.user = user
            new_order.save()
            new_order.products.set(selected_products)

            return Response(
                {
                    "message": "order confirm",
                    "order by": user.username,
                    "product": selected_products,
                }
            )

        return Response("something error")


class home_view(APIView):
    """User can loggin with username and password"""

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Used to return success message"""

        return Response({"message": "Welcome to the home view!"})
