from django.urls import path
from . import views

app_name = "mailings"

urlpatterns = [
    path("clients/", views.ClientListView.as_view(), name="client_list"),
]
