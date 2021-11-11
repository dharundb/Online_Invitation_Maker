from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse

def welcome(request):
    return render(request,'welcome.html')

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if(len(username)==0 or len(password)==0):
            messages.info(request,'Do not leave Credentials empty!')
            return HttpResponseRedirect('/login')
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request,'Username does not exist.')
                return HttpResponseRedirect('/login')
            elif user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/stylings')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')

    return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        if(len(username)==0 or len(email)==0 or len(pwd1)==0 or len(pwd2)==0):
            messages.info(request,"Don't leave the credentials empty!")
            return redirect('signup')
        elif(len(pwd1)<8 or len(pwd2)<8):
            messages.info(request,'Password should contain atleast 8 characters!')
            return redirect('signup')
        if(pwd1==pwd2):
            if (User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists()):
                messages.info(request,"Username and email already exists!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists(): #checks whether email is already in use
                messages.info(request,"This email already exists!")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists!")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=pwd1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords are not same')
            return redirect('signup')

    return render(request,'signup.html')

