from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', views.sample, name='sample'),
    #path('', TemplateView.as_view(template_name='index.html'), name='sample'),
    path('login/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]