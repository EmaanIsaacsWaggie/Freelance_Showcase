from django.shortcuts import render, redirect, get_object_or_404
from .models import Work
from .forms import workform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
import os

@login_required(login_url="/accounts/")
def upload_work(request):
    if request.method == 'POST':
        form = workform(request.POST, request.FILES)
        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user
            work.save()  # Saves the uploaded file automatically
            messages.success(request, 'File uploaded successfully.')
        return redirect('projects:upload_work')  # Redirect to the same page after upload
    else:
        form = workform()

    # List all files in the MEDIA_ROOT for download links
    available_files = os.listdir(settings.MEDIA_ROOT)

    # Render the upload work page with the form and available files
    return render(request, 'projects/upload_work.html', {'form': form, 'available_files': available_files})

def home(request):
    # Render the home page
    return render(request, 'projects/home.html')

def projects(request):
    # Retrieve all work objects
    works = Work.objects.all()  
    # Render the projects page with the list of works
    return render(request, 'projects/project.html', {'works': works})

@login_required(login_url="/accounts/")
def delete_project(request, pk):
    # Handle project deletion
    if request.method == 'POST':
        work = get_object_or_404(Work, pk=pk)  # Get the work object or return a 404 error
        work.delete()  # Delete the work object
        return redirect('projects:projects')  # Redirect back to the projects page after deletion
    # Redirect in case of a GET request
    return redirect('projects:projects')
