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
        fields = '__all__'
    
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ["stage", "job_title", "deadline", "job_description", "job_url", "job_email"]
        
    def clean(self):
 
        # data from the form is fetched using super function
        super(EditPostForm, self).clean()
         
        # extract the username and text field from the data
        stage = self.cleaned_data.get('stage')
        job_title = self.cleaned_data.get('job_title')

        text = self.cleaned_data.get('text')
 
        # conditions to be met for the username length
        if stage is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
        if job_title is None:
            self._errors['stage'] = self.error_class([
                'Required Field'])
 
        # return any errors if found
        return self.cleaned_data