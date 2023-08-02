from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import UserRegistrationForm


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer

# make views for input data from HTMl from browser api
class UserRegistrationView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
            user.save()
        return response
#print(check_password("hellotest","pbkdf2_sha256$600000$YMjassgoudr5ekMLfsmrgD$2tl9zj60V8NY9HX973Jl49srRpKXJ5VhJnNEjCjfn8E="))


#make view for input data JSON from postman
class User_Registration_View(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'message': "user is created"
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
