from django.urls import path

from .views import roster, players, coaches

urlpatterns = [
        path('', roster.home, name='home'),
        ]
