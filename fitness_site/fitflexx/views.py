from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Class


def index(request):
    return render(request, 'index.html')

def classes(request):
    # Retrieve the list of classes from the database
    class_list = Class.objects.all()
    
    # Pass the classes to the template
    return render(request, 'classes.html', {'classes': class_list})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def book_class(request, class_id):
    # Retrieve the selected class
    selected_class = Class.objects.get(id=class_id)
    
    # Perform validations or checks here
    
    # Save the class booking details in the database
    
    return redirect('success')  # Redirect to a success page or appropriate URL


@login_required
def notifications(request):
    # Retrieve the logged-in user's notifications
    user_notifications = request.user.notifications.all()
    
    return render(request, 'notifications.html', {'notifications': user_notifications})


@login_required
def user_profile(request):
    # Retrieve the logged-in user's profile details
    user_profile = request.user.profile
    
    return render(request, 'profile.html', {'profile': user_profile})
