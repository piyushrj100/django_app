from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request) :
    projects =Project.objects.all()
    msg= 'Hello you are on the projects page'
    number=10
    context ={'projects' : projects}
    return render(request, 'projects/projects.html',context) #passing the message as dictionary to be used in the html template

def project(request,pk) :
    # return HttpResponse('SINGLE PROJECT' + " " +str(pk))
    projectObj=Project.objects.get(id=pk)
    # tags=projectObj.tags.all()
    return render(request,'projects/single-project.html', {'project' : projectObj} )

# def createProject(request) :
#     context={}
#     return render(request, "projects/project_form.html", context)

def createProject(request) :
    form = ProjectForm()
    context={'form' : form} 
    return render(request, "projects/project_form.html", context)

