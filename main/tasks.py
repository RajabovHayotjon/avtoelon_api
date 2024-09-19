

from celery import shared_task
from time import sleep

from django.core.mail import send_mail

@shared_task
def send_email():
    send_mail('Test mail', 'this is a test email', 'askarjon.abdullayev@gmail.com', ['rajabovhayotjon777@gmail.com'],fail_silently=False)

    return 1

@shared_task
def longtime_add(x, y):
    sleep(10)
    return x + y
