from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TweetForm,ReplyForm,MessageForm
from .serializers import TweetSerializer
from .models import Tweet,TweetReply,Message
from authentication.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes,permission_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated



 
# Create your views here.
'''
@login_required(login_url='login')
def tweet(request):
    user = request.user
    print(user.first_name)
    Tweets_data = Tweet.objects.all()
    TweetReplys_data = TweetReply.objects.all()
    if request.method == "POST":
        print('post')
        form = TweetForm(request.POST,user=user)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('save')
            form.save()

    form = TweetForm(user=user)
    context={'form':form,'user':user,'Tweets_data':Tweets_data,'TweetReplys_data':TweetReplys_data}
    return render(request,'tweet.html',context)
'''
@api_view(['GET'])
@permission_classes([IsAuthenticated])
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def tweet(request):
    Tweets_data = Tweet.objects.all()
    Tweets_data = TweetSerializer(Tweets_data, many=True)
    return Response(Tweets_data.data,template_name='tweet.html')


def get_users(user,opp_user):
    exclude_ids = [user.id,opp_user.id]
    users_data = User.objects.exclude(id__in=exclude_ids)
    return users_data

@login_required(login_url='login')
def reply(request, pk):
    user = request.user
    print(user.first_name)
    Tweets_data = Tweet.objects.filter(id=pk)
    tweet=Tweets_data.first()
    print(tweet)
    if request.method == "POST":
        print('post')
        form=ReplyForm(request.POST,user=user,tweet=tweet)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('save')
            form.save()
    form=ReplyForm(user=user,tweet=tweet)
    context = {'form':form}
    return render(request,'reply.html',context)

@login_required(login_url='login')
def message(request, pk):
    user = request.user
    print(user.first_name)

    opp_user = User.objects.filter(id=pk).first()
    print(opp_user)

    Messages_data_receiver = Message.objects.filter(user=opp_user).filter(opp_user=user)
    Messages_data_sender = Message.objects.filter(user=user).filter(opp_user=opp_user)
    Messages_data = Messages_data_sender.union(Messages_data_receiver)
    Messages_data = Messages_data.order_by('created_at')
    
    users_data =get_users(user,opp_user)

    if request.method == "POST":
        print('post')
        form=MessageForm(request.POST,user=user,opp_user=opp_user)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('save')
            form.save()
    form=MessageForm(user=user,opp_user=opp_user)
    context = {'form':form,'Messages_data':Messages_data, 'user':user, 'opp_user':opp_user, 'users_data':users_data}
    return render(request,'message.html',context)