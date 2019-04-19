from django.urls import include, path

from .views import roster, players, coaches

urlpatterns = [
        path('', roster.home, name='home'),

        path('coaches/', include(([
            path('', coaches.TeamListView.as_view(), name='team_change_list'),
            #path('team/add/', coaches.TeamCreateView.as_view(), name='team_add'),
            #path('team/<int:pk>', coaches.TeamUpdateView.as_view(), name='team_change'),
            
            ], 'roster'), namespace='coaches')),

]
       
