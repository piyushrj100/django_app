# Create your views here.
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def loginPage(request) :
    if request.method=="POST" :
        username=request.POST['username']
        password=request.POST['password']

        try :
            user=User.objects.get(username=username)
        except:
            print("Username does not exist")
        user=authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            return redirect('profiles')
        else :
            print("username or password is incorrect")

    return render(request,'users/login_register.html')


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

