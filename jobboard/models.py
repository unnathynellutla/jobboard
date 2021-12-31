from django.db import models
from django.utils import timezone


class Stage(models.Model):
    stage_title = models.CharField(max_length=200)
    def __str__(self):
        return self.stage_title

    def ordered_posting_set(self):
        return self.posting_set.all().order_by('deadline')
        
class Posting(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=True, null=True)
    job_title = models.CharField(max_length=200, blank=True, null=True)
    deadline = models.DateTimeField('Next Deadline', blank=True, null=True)
    job_description = models.TextField('Descripton', blank=True, null=True)
    job_url = models.URLField(max_length=200, blank=True, default = '')
    job_email = models.CharField('email', max_length=200, blank=True, default = '')
    def __str__(self):
        return self.job_title
    def date_passed(self):
        return self.deadline <= timezone.now()

