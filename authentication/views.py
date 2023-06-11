from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from connections.models import Tweet,TweetReply
 



# Create your views here.
def sample(request):
    return render(request,'index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('connections:tweet')
        else:
            messages.info(request,'Username or password is incorrect')

    return render(request,'index.html')

def signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('save')
            form.save()
    print('Hi2')      
    context={'form':form}
    return render(request,'index.html',context)

def signout(request):
    logout(request)
    return redirect('sample')