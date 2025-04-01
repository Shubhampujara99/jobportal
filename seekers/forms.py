from django import forms
from .models import Bookmark, Alert

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['job']

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['keyword', 'location', 'job_type']