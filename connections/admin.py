from django.contrib import admin
from .models import Tweet,TweetReply,Message


# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ['id','user','tweet','created_at']

class TweetReplyAdmin(admin.ModelAdmin):
    list_display = ['id','user','tweet','get_tweet_user','reply','created_at']

    def get_tweet_user(self, obj):
        return obj.tweet.user

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id','user','opp_user','message','created_at']

admin.site.register(Tweet,TweetAdmin)
admin.site.register(TweetReply,TweetReplyAdmin)
admin.site.register(Message,MessageAdmin)
