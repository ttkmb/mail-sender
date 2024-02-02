from datetime import datetime
import smtplib

from django.conf import settings
from django.core.mail import send_mail
from mailer.models import MailerLogger, Mailer


def send_mail_and_log(mail_setting: Mailer, client: Mailer.clients):
    """
    Отправка письма с логированием
    """
    mail = mail_setting.mail
    status = MailerLogger.STATUS.SUCCESS
    error_msg = None
    try:
        send_mail(
            subject=mail.title,
            message=mail.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client],
        )
    except smtplib.SMTPException as e:
        error_msg = e
        status = MailerLogger.STATUS.FAILED
    except Exception as e:
        error_msg = e
        status = MailerLogger.STATUS.FAILED
    finally:
        log = MailerLogger.objects.create(
            status=status,
            response=error_msg,
        )
        log.save()


def process_mailer_tasks():
    """
    Проверка логики рассылок, изменение статуса рассылки, отправка письма
    """
    time_now = datetime.now().astimezone(None)
    mails = Mailer.objects.filter(status='CREATED', time_start__lte=time_now, time_stop__gte=time_now)
    for mail in mails:
        mail.status = 'LAUNCHED'
        mail.save()

    mails_settings = Mailer.objects.filter(status='LAUNCHED')
    for mail_setting in mails_settings:
        time_start = mail_setting.time_start
        time_stop = mail_setting.time_stop
        if time_start <= time_now <= time_stop:
            for client in mail_setting.clients.all():
                send_mail_and_log(mail_setting, client)
        if time_now >= time_stop:
            mail_setting.status = 'COMPLETE'
            mail_setting.save()
        mail_setting.save()