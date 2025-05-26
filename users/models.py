from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = None                       # убираем username
    email = models.EmailField("e-mail", unique=True)

    avatar = models.ImageField("аватар", upload_to="avatars/", blank=True)
    phone  = models.CharField("телефон", max_length=30, blank=True)
    country = models.CharField("страна", max_length=64, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []       # только e-mail и пароль

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self) -> str:             # админка / shell-plus
        return self.email
