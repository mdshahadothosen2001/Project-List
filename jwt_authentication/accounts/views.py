from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import UserRegistrationForm

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
            user.set_password(make_password(password))
            user.save()
        return response