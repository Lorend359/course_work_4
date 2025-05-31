from django.core.management.base import BaseCommand
from django.utils import timezone
from mailings.models import Mailing, MailingAttempt
from django.core.mail import send_mail


class Command(BaseCommand):
    help = "Отправляет рассылки, у которых наступило время отправки"

    def handle(self, *args, **options):
        now = timezone.now()
        mailings = Mailing.objects.filter(status="Создана", start_time__lte=now, end_time__gte=now)

        for mailing in mailings:
            success, failed = 0, 0
            for client in mailing.clients.filter(owner=mailing.owner):
                try:
                    send_mail(
                        subject=mailing.message.subject,
                        message=mailing.message.body,
                        from_email="from@example.com",
                        recipient_list=[client.email],
                        fail_silently=False,
                    )
                    MailingAttempt.objects.create(
                        mailing=mailing, status="Успешно", server_response="Отправлено без ошибок"
                    )
                    success += 1
                except Exception as e:
                    MailingAttempt.objects.create(mailing=mailing, status="Не успешно", server_response=str(e))
                    failed += 1

            mailing.status = "Запущена"
            mailing.save()
            self.stdout.write(
                self.style.SUCCESS(f"Рассылка {mailing.pk} отправлена: {success} успешно, {failed} ошибок")
            )
