from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from .settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from jobboard.models import Stage
from datetime import date, timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
app = Celery('mysite')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task
def add(x, y):
    return x + y

@app.task
def daily_emails():
    receivers = "unnathy.nellutla@tufts.edu"
    current_day = date.today()
    subject= "Today's Job Alerts for "
    message = 'Your deadlines in the next 24 hours: '
    send_mail(subject,message,EMAIL_HOST_USER,[receivers], fail_silently= False)
    return('first_task_done')