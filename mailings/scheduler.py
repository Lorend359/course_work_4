from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.core.management import call_command
import logging

logger = logging.getLogger(__name__)


def scheduled_job():
    logger.info("Выполняем запланированную отправку рассылок")
    call_command("send_scheduled_mailings")


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(scheduled_job, "interval", minutes=1, name="send_mailings")
    scheduler.start()
