from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BaseSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class JobSeekerSignUpForm(BaseSignUpForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1  # Job Seeker
        if commit:
            user.save()
        return user

class EmployerSignUpForm(BaseSignUpForm):
    company_name = forms.CharField(max_length=100)
    company_description = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2  # Employer
        if commit:
            user.save()
        return user