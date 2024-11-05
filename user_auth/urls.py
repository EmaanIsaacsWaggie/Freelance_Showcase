from django.urls import path  # Import path function for URL routing
from . import views  # Import views from the current directory
from django.contrib.auth.views import LogoutView  # Import the built-in LogoutView

app_name = 'user_auth'  # Namespace for the user authentication app

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),  # URL for the login page
    path('show_user/', views.show_user, name='show_user'),  # URL to display user information
    path('register/', views.register, name='register'),  # URL for user registration
    path('logout/', LogoutView.as_view(next_page='user_auth:login'), name='logout'),  # URL to log out and redirect to the login page
]
