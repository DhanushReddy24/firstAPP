from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Tweet,TweetReply,Message


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('user','tweet',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        if user:
            self.fields['user'].initial = user

class ReplyForm(forms.ModelForm):
    class Meta:
        model = TweetReply
        fields = ('user','tweet','reply',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        tweet = kwargs.pop('tweet', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['tweet'].widget = forms.HiddenInput()
        if user:
            self.fields['user'].initial = user
        if tweet:
            self.fields['tweet'].initial = tweet

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('user','opp_user','message',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        opp_user = kwargs.pop('opp_user', None)
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()
        self.fields['opp_user'].widget = forms.HiddenInput()
        if user:
            self.fields['user'].initial = user
        if opp_user:
            self.fields['opp_user'].initial = opp_user