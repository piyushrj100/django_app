# Create your views here.
from django.shortcuts import render
from .models import Profile
def profiles(request) :
    return render(request, "users/profiles.html")

def profiles(request) :
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context)

def userProfile(request,pk) :
    profile=Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(description__exact="") #accessing the child model skill and filter all skills that is not empty 
    otherskills=profile.skill_set.filter(description="")
    context={'profile':profile,'topskills':topskills,'otherskills':otherskills}
    return render(request,'users/user-profile.html',context)
