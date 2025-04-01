from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Job Seeker'),
        (2, 'Employer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)  # Add null/blank
    phone = models.CharField(max_length=20, null=True, blank=True)  # Add null/blank
    is_verified = models.BooleanField(default=False)

class JobSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()
    company_logo = models.ImageField(upload_to='company_logos/')

    def __str__(self):
        return self.username
    
