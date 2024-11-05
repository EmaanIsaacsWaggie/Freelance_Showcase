from django.urls import path  # Import path function for URL routing
from . import views  # Import views from the current directory

app_name = 'projects'  # Namespace for the app

urlpatterns = [
    path('', views.home, name='home'),  # URL for the home page
    path('upload/', views.upload_work, name='upload_work'),  # URL to upload work
    path('projects/', views.projects, name='projects'),  # URL to view all projects
    path('delete/<int:pk>/', views.delete_project, name='delete_project'),  # URL to delete a specific project
]
