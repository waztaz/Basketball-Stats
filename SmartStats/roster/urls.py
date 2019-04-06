from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('home', views.home, name='home'),
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        #ex: /roster/team/5/player/4
        #path('team/<int:team_id>/player/<int:player_id>', views.player, name='player'),
        path('', views.coach, name='coach'),
        #path('', views.team, name='team'),
        #path('game_id', 'player_id', views.player, name='player')
        ]
