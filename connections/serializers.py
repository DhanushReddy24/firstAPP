from rest_framework import serializers
from .models import Tweet,TweetReply,Message

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'