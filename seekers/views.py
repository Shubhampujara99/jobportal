from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job, Application
from .models import Bookmark, Alert
from .forms import BookmarkForm, AlertForm

@login_required
def seeker_dashboard(request):
    if not request.user.user_type == 1:
        return redirect('home')
    
    seeker = request.user.jobseeker
    applications = Application.objects.filter(seeker=seeker)
    bookmarks = Bookmark.objects.filter(seeker=seeker)
    alerts = Alert.objects.filter(seeker=seeker, is_active=True)
    
    return render(request, 'seekers/dashboard.html', {
        'applications': applications,
        'bookmarks': bookmarks,
        'alerts': alerts
    })

@login_required
def add_bookmark(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(pk=job_id)
        seeker = request.user.jobseeker
        Bookmark.objects.get_or_create(seeker=seeker, job=job)
        return redirect('job_detail', job_id=job_id)
    return redirect('job_list')