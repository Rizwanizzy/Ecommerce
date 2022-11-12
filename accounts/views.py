from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


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
                return redirect(request, 'register')
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