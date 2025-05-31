from django.db import models
from django.conf import settings


class Client(models.Model):
    email = models.EmailField("e-mail", unique=True)
    full_name = models.CharField("Ф. И. О.", max_length=255)
    comment = models.TextField("Комментарий", blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец", related_name="clients"
    )

    class Meta:
        verbose_name = "получатель рассылки"
        verbose_name_plural = "получатели рассылки"

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Message(models.Model):
    subject = models.CharField("Тема письма", max_length=255)
    body = models.TextField("Тело письма")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец", related_name="messages"
    )

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("Создана", "Создана"),
        ("Запущена", "Запущена"),
        ("Завершена", "Завершена"),
    ]

    start_time = models.DateTimeField("Начало рассылки")
    end_time = models.DateTimeField("Окончание рассылки")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="Создана")

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", related_name="mailings")
    clients = models.ManyToManyField(Client, verbose_name="Получатели", related_name="mailings")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец", related_name="mailings"
    )

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"

    def __str__(self):
        return f"Рассылка от {self.start_time} до {self.end_time} — {self.status}"


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ("Успешно", "Успешно"),
        ("Не успешно", "Не успешно"),
    ]

    attempt_time = models.DateTimeField("Дата и время попытки", auto_now_add=True)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField("Ответ почтового сервера")

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Рассылка", related_name="attempts")

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылок"

    def __str__(self):
        return f"{self.attempt_time} — {self.status}"
