from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from .models import Client, Message, Mailing, MailingAttempt
from .forms import MailingForm


# ===== КЛИЕНТЫ =====
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
    template_name = "mailings/client_form.html"
    fields = ["email", "full_name", "comment"]
    success_url = reverse_lazy("mailings:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "mailings/client_confirm_delete.html"
    success_url = reverse_lazy("mailings:client_list")


# ===== СООБЩЕНИЯ =====
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


# ===== РАССЫЛКИ =====
class MailingListView(ListView):
    model = Mailing
    template_name = "mailings/mailing_list.html"
    context_object_name = "mailings"


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


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailings/mailing_confirm_delete.html"
    success_url = reverse_lazy("mailings:mailing_list")


class MailingSendView(View):
    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        success_count = 0
        error_count = 0

        for client in mailing.clients.all():
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email="from@example.com",
                    recipient_list=[client.email],
                    fail_silently=False,
                )
                MailingAttempt.objects.create(
                    mailing=mailing,
                    status="Успешно",
                    server_response="Отправлено без ошибок",
                )
                success_count += 1
            except Exception as e:
                MailingAttempt.objects.create(
                    mailing=mailing,
                    status="Не успешно",
                    server_response=str(e),
                )
                error_count += 1

        mailing.status = "Запущена"
        mailing.save(update_fields=["status"])
        messages.success(
            request,
            f"Отправка завершена: Успешно — {success_count}, Ошибки — {error_count}"
        )
        return redirect("mailings:mailing_list")


# ===== ПОПЫТКИ РАССЫЛОК =====
class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = "mailings/attempt_list.html"
    context_object_name = "attempts"


# ===== ГЛАВНАЯ СТРАНИЦА =====
class HomeView(TemplateView):
    template_name = "mailings/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_mailings"] = Mailing.objects.count()
        context["active_mailings"] = Mailing.objects.filter(status="Запущена").count()
        context["unique_clients"] = Client.objects.count()
        return context
