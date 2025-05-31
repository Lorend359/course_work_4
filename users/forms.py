from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "avatar", "phone", "country")


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail")
