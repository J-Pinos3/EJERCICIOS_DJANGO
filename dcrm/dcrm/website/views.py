from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):

    #check to see if user is logged in, I get what's inside form's login boxes
    if request.method == 'POST':
        username =  request.POST['username']
        password =  request.POST['password']

        #authenticate
        user = authenticate(request, username=username, password=password)
        #user is not empty or null
        if user is not None: 
            login(request, user)
            messages.success(request, "You've been logged in.")
            return redirect('home')
        else:
            messages.success(request, "Something went wrong, Please try again.")
            return redirect('home')
            
    else:
        return render(request, 'home.html', {})

"""
def login_user(request):
    pass
"""

def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})