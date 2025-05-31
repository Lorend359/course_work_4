from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from .forms import UserRegisterForm, UserLoginForm
from .models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

class UserRegisterView(CreateView):
    model = CustomUser
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        user = form.instance

        print("===> Sending email to:", user.email)
        print("From:", settings.DEFAULT_FROM_EMAIL)
        print("Using backend:", settings.EMAIL_BACKEND)

        send_mail(
            subject="Добро пожаловать!",
            message="Вы успешно зарегистрировались на сервисе рассылок.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return response


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"


class UserLogoutView(View):
    next_page = reverse_lazy("mailings:home")

    def get(self, request):
        logout(request)
        return redirect(self.next_page)


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ("avatar", "phone", "country")
    template_name = "users/update.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user
