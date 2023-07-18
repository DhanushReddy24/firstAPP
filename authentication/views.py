from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from connections.models import Tweet,TweetReply
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view, renderer_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response



 



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


@api_view(['POST'])
def signup(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data = request.POST)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

def signout(request):
    logout(request)
    return redirect('sample')