from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Message, Mailing
from .forms import MailingForm


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


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "mailings/client_confirm_delete.html"
    success_url = reverse_lazy("mailings:client_list")


class MessageListView(ListView):
    model = Message
    template_name = "mailings/message_list.html"
    context_object_name = "messages"


class MessageCreateView(CreateView):
    model = Message
    template_name = "mailings/message_form.html"
    fields = ["subject", "body"]
    success_url = reverse_lazy("mailings:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    template_name = "mailings/message_form.html"
    fields = ["subject", "body"]
    success_url = reverse_lazy("mailings:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "mailings/message_confirm_delete.html"
    success_url = reverse_lazy("mailings:message_list")


class MailingListView(ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"
    context_object_name = "mailings"


class MailingCreateView(CreateView):
    model = Mailing
    template_name = "mailings/mailing_form.html"
    fields = ["start_time", "end_time", "status", "message", "clients"]
    success_url = reverse_lazy("mailings:mailing_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    template_name = "mailings/mailing_form.html"
    fields = ["start_time", "end_time", "status", "message", "clients"]
    success_url = reverse_lazy("mailings:mailing_list")


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailings/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailings:mailing_list")


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailings/mailing_form.html"
    success_url = reverse_lazy("mailings:mailing_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = "mailings/mailing_form.html"
    success_url = reverse_lazy("mailings:mailing_list")
