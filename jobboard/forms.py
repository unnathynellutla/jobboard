from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Posting, Stage

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
        fields = ['stage', 'job_title', 'deadline', 'job_description', 'job_url', 'job_email']

    def __init__(self, * args, ** kwargs):
        self.request = kwargs.pop("request")
        super(EditPostForm, self).__init__( * args, ** kwargs)
        self.fields["stage"].queryset = Stage.objects.filter(author = self.request.user)
    
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