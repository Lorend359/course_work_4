from django.db import models


class Client(models.Model):
    email = models.EmailField("e-mail", unique=True)
    full_name = models.CharField("Ф. И. О.", max_length=255)
    comment = models.TextField("Комментарий", blank=True)

    class Meta:
        verbose_name = "получатель рассылки"
        verbose_name_plural = "получатели рассылки"

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Message(models.Model):
    subject = models.CharField("Тема письма", max_length=255)
    body = models.TextField("Тело письма")

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"

    def __str__(self):
        return self.subject
