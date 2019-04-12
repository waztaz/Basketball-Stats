from django.urls import path

from . import views

urlpatterns = [
        #ex: /roster/
        path('', views.index, name='index'),
        #ex: /roster/home
        path('home', views.home, name='home'),
        #ex: /roster/register
        path('register', views.register, name='register'),
        #ex:/roster/login
        path('login', views.login, name='login'),
        #ex: /roster/team/5
        path('team/<int:team_id>/', views.team, name='team'),
        #ex: /roster/team/5/player/4
        path('team/<int:team_id>/player/<int:player_id>', views.player, name='player'),
        #ex:/roster/team/5/coach/4
        path('', views.coach, name='coach'),
        path('realtimetracker', views.realtimetracker, name = 'realtimetracker')
        #path('', views.team, name='team'),
        #path('game_id', 'player_id', views.player, name='player')
        ]
