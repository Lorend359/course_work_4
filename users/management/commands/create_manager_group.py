from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser
from mailings.models import Client, Mailing


class Command(BaseCommand):
    help = "Создаёт группу 'Менеджеры' и назначает ей базовые права."

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Менеджеры")
        if created:
            self.stdout.write(self.style.SUCCESS("Группа 'Менеджеры' создана."))
        else:
            self.stdout.write("Группа 'Менеджеры' уже существует.")

        # Разрешения на просмотр клиентов и рассылок
        permissions = []

        for model in [Client, Mailing]:
            content_type = ContentType.objects.get_for_model(model)
            view_perm = Permission.objects.get(codename=f"view_{model._meta.model_name}", content_type=content_type)
            permissions.append(view_perm)

        # Разрешение на просмотр и изменение пользователей
        user_ct = ContentType.objects.get_for_model(CustomUser)
        view_user = Permission.objects.get(codename="view_customuser", content_type=user_ct)
        change_user = Permission.objects.get(codename="change_customuser", content_type=user_ct)
        permissions.extend([view_user, change_user])

        group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS("Права назначены группе 'Менеджеры'."))
