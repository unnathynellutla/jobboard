from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Posting, Stage, UpdateTime
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class EditStageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ['author', 'stage_title']

    def __init__(self, * args, ** kwargs):
        self.request = kwargs.pop("request")
        super(EditStageForm, self).__init__( * args, ** kwargs)
        self.fields["author"].initial = self.request.user
        self.fields["author"].widget = forms.HiddenInput()
    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['stage', 'company', 'job_title', 'deadline', 'job_description', 'job_url', 'job_email']

    def __init__(self, * args, ** kwargs):
        self.request = kwargs.pop("request")
        super(EditPostForm, self).__init__( * args, ** kwargs)
        self.fields["stage"].queryset = Stage.objects.filter(author = self.request.user)
        self.fields["job_description"].strip = False
    
    def clean(self):
        super(EditPostForm, self).clean()
         
        stage = self.cleaned_data.get('stage')
        job_title = self.cleaned_data.get('job_title')
 
        if stage is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
        if job_title is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
 
        return self.cleaned_data

class UpdateTimeForm(forms.ModelForm):
    class Meta:
        model = UpdateTime
        fields = '__all__'

    def __init__(self, * args, ** kwargs):
        self.request = kwargs.pop("request")
        super(UpdateTimeForm, self).__init__( * args, ** kwargs)
        self.fields["author"].initial = self.request.user
        self.fields["author"].widget = forms.HiddenInput()