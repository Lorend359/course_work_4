from django.urls import path
from .views import UserRegisterView, UserLogoutView, UserProfileView, UserUpdateView
from .forms import UserLoginForm
from django.contrib.auth.views import LoginView

app_name = "users"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path(
        "login/", LoginView.as_view(template_name="users/login.html", authentication_form=UserLoginForm), name="login"
    ),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/edit/", UserUpdateView.as_view(), name="edit_profile"),
]
