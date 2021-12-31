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
        fields = ['stage_title']
    
class EditPostForm(forms.ModelForm):

    stage = forms.ModelMultipleChoiceField(queryset = None)
    job_title = forms.CharField(max_length=200)
    deadline = forms.DateTimeField(required=False)
    job_description = forms.CharField(widget=forms.Textarea, required=False)
    job_url = forms.URLField(initial='http://', required=False)
    job_email = forms.EmailField(required=False)

    def __init__(self, * args, ** kwargs):
        self.request = kwargs.pop("request")
        super(EditPostForm, self).__init__( * args, ** kwargs)
        self.fields["stage"].queryset = Stage.objects.filter(author = self.request.user)
    
    def clean(self):
 
        # data from the form is fetched using super function
        super(EditPostForm, self).clean()
         
        # extract the username and text field from the data
        stage = self.cleaned_data.get('stage')
        job_title = self.cleaned_data.get('job_title')
 
        # conditions to be met for the username length
        if stage is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
        if job_title is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
 
        # return any errors if found
        return self.cleaned_data