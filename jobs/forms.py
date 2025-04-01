from django import forms
from .models import Job

class JobSearchForm(forms.Form):
    keyword = forms.CharField(required=False)
    location = forms.CharField(required=False)
    job_type = forms.ChoiceField(
        choices=Job.JOB_TYPES, 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

# Move ApplicationForm to models.py as ModelForm