from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserRegisterView
from .forms import UserLoginForm

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(
        template_name="users/login.html",
        authentication_form=UserLoginForm
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="mailings:home"), name="logout"),
]
