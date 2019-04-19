from django.urls import include, path

from .views import roster, players, coaches

urlpatterns = [
        path('', roster.home, name='home'),

        path('coaches/', include(([
            path('', coaches.TeamListView.as_view(), name='team_list'),
            path('team/add/', coaches.TeamCreateView.as_view(), name='team_add'),
            path('team/<int:pk>', coaches.TeamUpdateView.as_view(), name='team_change'),
            path('team/<int:pk>/player/add', coaches.player_add, name='player_add'),
            path('team/<int:team_pk>/player/<int:player_pk>/', coaches.player_change, name='player_change')
            ], 'roster'), namespace='coaches')),

]
       
