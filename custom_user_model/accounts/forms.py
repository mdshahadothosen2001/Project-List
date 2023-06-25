# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    father_name = forms.CharField(max_length=30)
    mother_name = forms.CharField(max_length=30)
    brother_name = forms.CharField(max_length=30)
    sister_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    phone_number = forms.CharField(min_length=11, max_length=11)
    gender = forms.CharField(max_length=10)
    religion = forms.CharField(max_length=30)
    nationality = forms.CharField(max_length=30)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'father_name', 'mother_name', 'brother_name', 'sister_name', 'age', 'phone_number', 'email', 'gender', 'religion', 'nationality')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('Phone number is already registered.')
        return phone_number
