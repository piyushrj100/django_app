from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Project

projectList=[
    {
    'id' : '1', 
    'title' : "Ecommerce Website",
    'description' : 'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title' : "Portfolio Website",
        'description' :"This was a project that I built for my portfolio"
    },
    {
        'id' :'3',
        'title' : "Social Network",
        'description' : 'Awesome open source project I am still working on'
    },

]

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

