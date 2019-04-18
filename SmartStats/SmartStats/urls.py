"""SmartStats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
#from users import views as user_views
from roster.views import roster, players, coaches

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('roster.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', roster.SignUpView.as_view(), name='signup'),
    path('accounts/signup/player/', players.PlayerSignUpView.as_view(), name='player_signup'),
    path('accounts/signup/coach/', coaches.CoachSignUpView.as_view(), name='coach_signup'),
]
