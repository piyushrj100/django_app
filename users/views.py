# Create your views here.
from django.shortcuts import redirect, render
from .models import Profile
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm   

#Usercreation form for creating new users 
def loginUser(request) :
    if request.method=="POST" :
        username=request.POST['username']
        password=request.POST['password']

        try :
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user=authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            return redirect('profiles')
        else :
            messages.error(request, 'username or password is incorrect')

    return render(request,'users/login_register.html')
def logoutUser(request) :
    logout(request)
    messages.error(request, 'User logged out')
    return redirect('login')

def registerUser(request) :
    page='register'
    form=CustomUserCreationForm()
    if request.method == 'POST' :

        form=CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'User account was created!')
            login(request,user)
            return redirect('profiles')
        else :
            messages.success(request, 'An error has occured during registration')
    context={'page' : page, 'form' :form}
    return render(request, 'users/login_register.html', context)


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

@login_required(login_url='login')
def userAccount(request) :
    profile=request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context={'profile':profile,'skills':skills,'projects':projects}
    return render(request,'users/account.html', context)


