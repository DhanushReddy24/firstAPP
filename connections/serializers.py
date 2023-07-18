from rest_framework import serializers
from .models import Tweet,TweetReply,Message
from authentication.models import User


class TweetSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Tweet
        fields = ('id','user','tweet','created_at')

        def get_tweet_user(self, obj):
            return obj.user.first_name