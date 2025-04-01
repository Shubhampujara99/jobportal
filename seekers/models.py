from django.db import models
from accounts.models import JobSeeker
from jobs.models import Job

class Bookmark(models.Model):
    seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    seeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    job_type = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)