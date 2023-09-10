from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):

    records = Record.objects.all().values()

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
        return render(request, 'home.html', {'records':records})



"""
def login_user(request):
    pass
"""



def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authentica and login  ACORDING WITH forms.py
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You\'ve succesfully registered.')
            return redirect('home')
    else: 
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'recotd.html', {'customer_record':focustomer_record})
    else:
        messages.success(request, 'You must be logged in.')
        return redirect('home')