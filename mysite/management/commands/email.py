from django.core.management.base import BaseCommand, CommandError
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import datetime
from jobboard.models import Posting, Stage
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Sends an Email'

    def handle(self, *args, **options):
        send = False
        receivers = User.objects.all()
        current_day = datetime.now()
        for receiver in receivers:
            subject= "Today's Job Alerts for " + receiver.username
            message = 'Your deadlines in the next 24 hours: '
            for stage in Stage.objects.filter(author=receiver): 
                for posting in stage.ordered_posting_set():
                    if posting.deadline- datetime.timedelta(hours=24) <= current_day <= posting.deadline:
                        send = True
                        message += posting.job_title 
                        message += ' '
                        message += stage.stage_title
                        message += ' due on: '
                        message += posting.deadline.strftime("%m/%d/%Y, %H:%M:%S")
                        message += ' '
            if send == True:
                message += '.'
                send_mail(subject,message,EMAIL_HOST_USER,[receiver.email], fail_silently= False)
                send = False
        return('first_task_done')