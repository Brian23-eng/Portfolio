from django.shortcuts import render
from . models import Project

def home(request):
    title = "Portfolio"
    
    return render(request, 'index.html',{'title':title})

def project(request):
    title = "Portfolio"
    projects = Project.get_all_projects()
    return render(request, 'projects.html',{'projects':projects, 'title':title})


def project_detail(request, pk):
    title = "Portfolio"
    project = Project.objects.get(pk=pk)
    context = {
        'project': project,
        'title':title
    }
    return render(request, 'project_detail.html', context)
