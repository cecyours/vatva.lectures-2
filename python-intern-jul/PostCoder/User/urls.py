
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [ 
    path('singup',views.signup,name='sign-coder'),
    path('login',views.loginx,name='login-coder'),
    path('logout',views.logoutx,name='logout'),
    path('dashboard',views.user_dashboard,name='user-dashboard'),
    path('addpost',views.add_post,name='new_post'),

    path('',views.home,name='home')
]