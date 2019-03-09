from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        #ex: /roster/team/5/player/4
        path('team/<int:team_id>/player/<int:player_id>', views.player, name='player'),
        ]
