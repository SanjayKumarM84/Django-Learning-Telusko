from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        payload = request.POST
        username = payload.get('username', None)
        password = payload.get('password', None)

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':
        payload = request.POST
        first_name = payload.get('first_name', None)
        last_name = payload.get('last_name', None)
        username = payload.get('username', None)
        password1 = payload.get('password1', None)
        password2 = payload.get('password2', None)
        email = payload.get('email', None)

        if password1 != password2:
            messages.info(request,"Password Not Matching!!!!")
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,"UserName already taken!!!!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken!!!!!")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save();
                print("User Created!!!")
                return redirect('login')

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
