from django.core.management.base import BaseCommand, CommandError
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from datetime import date, timedelta
from jobboard.models import Posting, Stage
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Sends an Email'

    def handle(self, *args, **options):
        send = False
        receivers = User.objects.all()
        current_day = date.today()
        for receiver in receivers:
            subject= "Today's Job Alerts for " + receiver.username
            message = 'Your deadlines in the next 24 hours: '
            for stage in Stage.objects.filter(author=receiver): 
                for posting in stage.ordered_posting_set().filter(posting.deadline >= current_day-1):
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