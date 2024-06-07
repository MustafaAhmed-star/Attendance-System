from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feedback
from .forms import UserLoginForm, UserRegisterForm ,FeedbackForm






def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('/admin/')
                return redirect('/')   
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



#Feedback

@login_required
def submit_feedback(request):
    if request.user.is_student:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                feedback = form.save(commit=False)
                feedback.student = request.user
                feedback.save()
                messages.success(request, 'We will respond soon.')

                return redirect('view_feedback')
        else:
            form = FeedbackForm()
        return render(request, 'users/submit_feedback.html', {'form': form})
    else:
        return redirect('/')


@login_required
def view_feedback(request):
    feedbacks = Feedback.objects.filter(student=request.user).order_by('-created_at')
    return render(request, 'users/view_feedback.html', {'feedbacks': feedbacks})