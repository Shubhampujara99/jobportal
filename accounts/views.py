from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, JobSeekerSignUpForm, EmployerSignUpForm

# Login View
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 1:  # Job Seeker
                    return redirect('seeker_dashboard')
                else:  # Employer
                    return redirect('employer_dashboard')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

# Signup View
def signup(request):
    if request.method == 'POST':
        form_type = request.POST.get('user_type')
        if form_type == '1':  # Job Seeker
            form = JobSeekerSignUpForm(request.POST, request.FILES)
        else:  # Employer
            form = EmployerSignUpForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 1:
                return redirect('seeker_dashboard')
            else:
                return redirect('employer_dashboard')
    else:
        form = JobSeekerSignUpForm()  # Default form
    return render(request, 'accounts/signup.html', {'form': form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')