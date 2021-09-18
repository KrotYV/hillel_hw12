from celery import shared_task

from django.core.mail import send_mail as django_send_mail


@shared_task
def send_mail(email, message, date):
    django_send_mail(email, message, date, ['admin@example.com'])
