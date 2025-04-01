from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobSearchForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/detail.html', {'job': job})

@login_required
def job_search(request):
    form = JobSearchForm(request.GET or None)
    jobs = []
    
    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        location = form.cleaned_data.get('location')
        job_type = form.cleaned_data.get('job_type')
        
        jobs = Job.objects.filter(is_active=True, is_verified=True)
        
        if keyword:
            jobs = jobs.filter(title__icontains=keyword)
        if location:
            jobs = jobs.filter(location__icontains=location)
        if job_type:
            jobs = jobs.filter(job_type=job_type)
    
    return render(request, 'jobs/search.html', {'form': form, 'jobs': jobs})