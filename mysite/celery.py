from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from .settings import EMAIL_HOST_USER
from django.core.mail import send_mail
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
    send = False
    receivers = "unnathy.nellutla@tufts.edu"
    current_day = date.today()
    for receiver in receivers:
        subject= "Today's Job Alerts for " + receiver.username
        message = 'Your deadlines in the next 24 hours: '
        for stage in Stage.objects.filter(author=receiver): 
            for posting in stage.ordered_posting_set().filter(deadline__day=current_day):
                send = True
                message += posting.job_title 
                message += ' '
                message += stage.stage_title
                message += ' due on: '
                message += posting.deadline.strftime("%m/%d/%Y, %H:%M:%S")
                message += ' '
            message += '.'
        if send == True:
            send_mail(subject,message,EMAIL_HOST_USER,[receiver.email], fail_silently= False)
            send = False
    return('first_task_done')