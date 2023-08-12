from rest_framework import generics
from .models import User
from .serializers import UserAccountSerializer


class UserListCreateView(generics.ListCreateAPIView):
    """Display all users list"""

    queryset = User.objects.all()
    serializer_class = UserAccountSerializer