from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.sample, name='sample'),
    #path('', TemplateView.as_view(template_name='index.html'), name='sample'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
]