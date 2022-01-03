from django.core.management.base import BaseCommand, CommandError
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Sends an Email'

    def handle(self, *args, **options):
        receivers = "unnathy.nellutla@tufts.edu"
        current_day = date.today()
        subject= "Today's Job Alerts for "
        message = 'Your deadlines in the next 24 hours: '
        send_mail(subject,message,EMAIL_HOST_USER,[receivers], fail_silently= False)
        return('first_task_done')