from django.shortcuts import render
from . models import Project

def home(request):
    title = "Portfolio"
    
    return render(request, 'index.html',{'title':title})

def project(request):
    projects = Project.objects.all()
    
    context = {
        'projects':projects
    }
    
    return render(request, 'project.html', context)
