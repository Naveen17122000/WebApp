from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','is_staff','is_superuser']
