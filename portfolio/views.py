from django.shortcuts import render, redirect
from . models import Project

def home(request):
    title = "Portfolio"
    
    return render(request, 'index.html',{'title':title})

def project(request):
    title = "Portfolio"
    projects = Project.objects.all()
    context = {
        'projects':projects, 
        'title':title
    }
    return render(request, 'projects.html',locals())


def project_detail(request, pk):
    title = "Portfolio"
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'title':title
    }
    return render(request, 'project_detail.html', context)
