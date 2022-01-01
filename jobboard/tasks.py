from celery import shared_task 
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="send_email",
    ignore_result=True
)
def my_first_task():
    subject= 'Celery'
    message= 'My task done successfully'
    receiver= 'unnathy.nellutla@tufts.edu'
    send_mail(subject,message,EMAIL_HOST_USER,[receiver],
    fail_silently= False)
    return('first_task_done')