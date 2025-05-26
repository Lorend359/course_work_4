from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Client
from django.views.generic import UpdateView


class ClientListView(ListView):
    model = Client
    template_name = "mailings/client_list.html"
    context_object_name = "clients"


class ClientCreateView(CreateView):
    model = Client
    template_name = "mailings/client_form.html"
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("mailings:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    template_name = "mailings/client_form.html"  # используем тот же шаблон
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("mailings:client_list")
