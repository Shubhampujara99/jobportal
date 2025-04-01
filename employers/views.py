from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from jobs.models import Job, Application
from .forms import JobPostForm

@login_required
def employer_dashboard(request):
    if not request.user.user_type == 2:
        return redirect('home')
    
    employer = request.user.employer
    jobs = Job.objects.filter(employer=employer)
    applications = Application.objects.filter(job__employer=employer)
    
    return render(request, 'employers/dashboard.html', {
        'jobs': jobs,
        'applications': applications
    })

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employer
            job.save()
            return redirect('employer_dashboard')
    else:
        form = JobPostForm()
    return render(request, 'employers/post_job.html', {'form': form})