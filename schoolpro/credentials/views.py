from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")

    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=pass1,last_name=lname,first_name=fname,email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')