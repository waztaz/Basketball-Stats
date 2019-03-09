from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('player_id', 'game_id', views.basketballstats, name='basketballstats'),
        path('player_id', views.analytics, name='basketballstats')
        ]
