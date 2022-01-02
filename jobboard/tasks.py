from celery import shared_task 
from celery.decorators import periodic_task
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Stage
from datetime import date, timedelta


@periodic_task(
    run_every=timedelta(minutes=1),
    name="send_email_weekly",
    ignore_result=True
)
def weekly_emails():
    send = False
    receivers = User.objects.all()
    #current_week = date.today().isocalendar()[1]
    for receiver in receivers:
        subject= "Today's Job Alerts for " + receiver.username
        message = 'Your deadlines in the next week: '
       # for stage in Stage.objects.filter(author=receiver): 
       #     for posting in stage.ordered_posting_set().filter(deadline__week=current_week):
       #         send = True
       #         message += posting.job_title 
       #         message += ' '
       #         message += stage.stage_title
       #         message += ' due on: '
       #         message += posting.deadline.strftime("%m/%d/%Y, %H:%M:%S")
       #         message += ' '
       #     message += '.'
       # if send == True:
        send_mail(subject,message,EMAIL_HOST_USER,[receiver.email], fail_silently= False)
        send = False
    return('first_task_done')


@periodic_task(
    run_every=timedelta(minutes=1),
    name="send_email_daily",
    ignore_result=True
)
def daily_emails():
    send = False
    receivers = User.objects.all()
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