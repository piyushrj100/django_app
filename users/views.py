# Create your views here.
from django.shortcuts import render
from .models import Profile
def profiles(request) :
    return render(request, "users/profiles.html")

def profiles(request) :
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context)
