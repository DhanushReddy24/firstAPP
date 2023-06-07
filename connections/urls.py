from django.urls import path, include
from . import views


app_name = 'connections'

urlpatterns = [
    path('tweet/', views.tweet, name='tweet'),
    path('message/<int:pk>/', views.message, name='message'),
    path('reply/<int:pk>/', views.reply, name='reply'),
]