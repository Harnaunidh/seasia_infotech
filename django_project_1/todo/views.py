from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Task
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)  # Process form data when submitted
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegisterForm()  # Show an empty form when loading the page
    return render(request, 'todo/register.html', {'form': form})  # Render the form in the template



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)  # Authenticate user
        if form.is_valid():
            user = form.get_user()  # Get authenticated user
            login(request, user)  # Log in the user
            messages.success(request, f"Welcome {user.username}!")  # Show welcome message
            return redirect('todo')  # Redirect to task management page
    else:
        form = AuthenticationForm()  # Display an empty login form
    return render(request, 'todo/login.html', {'form': form})  # Render the login page



def user_logout(request):
    logout(request)  # Ends the user session
    return redirect('login')  # Redirects to login page



@login_required  # Restricts access to only logged-in users
def todo(request):
    tasks = Task.objects.filter(user=request.user)  # Show tasks only for the logged-in user
    if request.method == "POST":
        task_name = request.POST.get('task_name')
        task_deadline = request.POST.get('task_deadline')
        Task.objects.create(user=request.user, name=task_name, deadline=task_deadline)
        return redirect('todo')  # Refresh the page after adding a task
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

@login_required 
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('todo')  # Redirect back to the task list