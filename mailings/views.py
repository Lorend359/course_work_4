from django.views.generic import ListView
from .models import Client


class ClientListView(ListView):
    model = Client
    template_name = "mailings/client_list.html"
    context_object_name = "clients"
