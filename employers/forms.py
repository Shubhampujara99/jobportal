from django import forms
from .models import CompanyReview, InterviewSchedule

class CompanyReviewForm(forms.ModelForm):
    class Meta:
        model = CompanyReview
        fields = ['content', 'rating']

class InterviewForm(forms.ModelForm):
    class Meta:
        model = InterviewSchedule
        fields = ['date', 'notes']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }