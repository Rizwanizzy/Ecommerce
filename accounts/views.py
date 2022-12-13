from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import *


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username):
                messages.error(request, "Username has already taken")
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.error(request, "Email has already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name, username=username, email=email, password=password)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.error(request, "both passwords are different")
            print(password,password1)
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            print(username,password)
            messages.error(request,'invalid details')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    details=personaldetails.objects.filter(first_name=request.user).order_by('-id').first()
    # print(details)
    return render(request, 'user_profile.html',{'det':details})


def default_details(request):
    # if request.user is None:
    if request.method=='POST':
        gender=request.POST['gender']
        email=request.POST['email']
        number=request.POST['number']
        address=request.POST['address']
        details=personaldetails.objects.create(gender=gender,email=email,number=number,address=address,first_name=request.user)
        details.save()
        print("details:",request.user)
        return render(request,'user_profile.html',{'det':details})
    else:
        return render(request, 'default_details.html')
  