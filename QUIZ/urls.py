"""QUIZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from registration import views as registration_views
from USER import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/<quizname>', user_views.quiz, name='quiz' ),
    path('register/', registration_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('' , user_views.home , name='home'),
    path('dashboard/' , user_views.dashboard, name='dashboard'),
    path('leaderboard/' , user_views.leaderboard, name='leaderboard'),
    path('prevAns/', user_views.prevAns, name='prevAns'),
    path('result/<quizname>', user_views.result, name='result'),
    path('addQuestions/', user_views.addQuestions , name='addQuestions'),
    path('addquiz/', user_views.addquiz , name='addquiz'),
    path('accounts/', include('allauth.urls')),
    

]
