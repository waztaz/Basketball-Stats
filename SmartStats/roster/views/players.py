
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from ..forms import PlayerSignUpForm
from ..models import User, Coach, Team, Player, CumulativeStats, BasketballStat
from ..forms import CoachSignUpForm, PlayerForm

class PlayerSignUpView(CreateView):
    model = User
    form_class = PlayerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'player'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/accounts/login')

class PlayerStatsView(ListView):
    model = Player
    template_name = 'roster/players/player_home.html'

    def get_context_data(self, **kwargs):
        current_player = Player.objects.get(user = self.request.user)
        kwargs['player'] = current_player
        total_points = BasketballStat.objects.filter(player = current_player).aggregate(Sum('shot_value')).get('shot_value__sum', 0)
        kwargs['total_points'] = total_points
        total_rebounds = BasketballStat.objects.filter(player = current_player, event='rbd').count()
        kwargs['total_rebounds'] = total_rebounds
        total_assists = BasketballStat.objects.filter(player=current_player, event='ast').count()
        kwargs['total_assists'] = total_assists
        print(kwargs)
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        current_player = Player.objects.get(user = self.request.user)
        total_points = BasketballStat.objects.filter(player = current_player).aggregate(Sum('shot_value'))
        print(total_points)
        total_rebounds = BasketballStat.objects.filter(player = current_player, event='rbd').count()
        print(total_rebounds)
        total_assists = BasketballStat.objects.filter(player=current_player, event='ast').count()
        print(total_assists)
        return current_player
