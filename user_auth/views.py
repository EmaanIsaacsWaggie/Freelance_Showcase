from django.shortcuts import render, redirect  # Import necessary functions for views
from django.contrib.auth import login  # Import the login function for user authentication
from django.contrib.auth.forms import UserCreationForm  # Import the user creation form
from django.contrib import messages  # Import messages framework for feedback
from django.contrib.auth.views import LoginView  # Import the built-in LoginView

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'  # Set the template for the login page

    def form_valid(self, form):
        # Handle the form submission when it's valid
        login(self.request, form.get_user())  # Log the user in
        return redirect('user_auth:show_user')  # Redirect after successful login


def show_user(request):
    """
    Display the user's profile page.
    """
    if request.user.is_authenticated:
        # If the user is authenticated, render their profile
        return render(request, 'authentication/user.html', {
            "username": request.user.username,  # Pass the username to the template
        })
    else:
        # If not authenticated, redirect to the login page
        return redirect('user_auth:login')


def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in after registration
            return redirect('user_auth:show_user')  # Redirect after successful registration
    else:
        form = UserCreationForm()  # Create a new form instance for GET requests
    # Render the registration page with the form
    return render(request, 'authentication/register.html', {'form': form})
