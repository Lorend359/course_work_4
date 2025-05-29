from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser


class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"


class UserLogoutView(View):
    next_page = reverse_lazy("mailings:home")

    def get(self, request):
        logout(request)
        return redirect(self.next_page)
