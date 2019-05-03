
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..models import User, Coach, Team, Player, Game
from ..forms import CoachSignUpForm, PlayerForm, GameForm
from ..decorators import coach_required

class CoachSignUpView(CreateView):
    model = User
    form_class = CoachSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'coach'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('/accounts/login')


@method_decorator([login_required, coach_required], name='dispatch')
class TeamListView(ListView):
    model = Team
    ordering = ('name', )
    #context_object_name = 'team'
    template_name = 'roster/coaches/team_list.html'

    def get_context_data(self, **kwargs):
        kwargs['coach'] = Coach.objects.filter(user=self.request.user)[0]
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user)
        print(current_coach)
        queryset = Team.objects.filter(coach_id=current_coach) \
                .annotate(player_count=Count('players', distinct=True))
        print(queryset)
        return queryset

@method_decorator([login_required, coach_required], name='dispatch')
class PlayerListView(ListView):
    model = Player
    ordering = ('first_name', 'last_name', )
    template_name = 'roster/coaches/team_change_form.html'

    def get_queryset(self):
        queryset=Player.objects.filter(team=self.kwargs.get('pk'))
        print(queryset)
        return queryset

@method_decorator([login_required, coach_required], name='dispatch')
class TeamUpdateView(UpdateView):
    model=Team
    fields = ('name', 'coach_id', )
    template_name = 'roster/coaches/team_change_form.html'

    def get_context_data(self, **kwargs):
        kwargs['players'] = self.get_object().players
        print("hello" + str(kwargs))
        #kwargs['team'] = self.get_object().name
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user)
        print(current_coach)
        queryset = Team.objects.filter(coach_id=current_coach)
        print("hello" + str(queryset))
        return queryset

    def get_success_url(self):
        return reverse('coaches:team_change', kwargs={'pk': self.object.pk})

@method_decorator([login_required, coach_required], name='dispatch')
class GameListView(ListView):
    model=Game
    template_name = 'roster/coaches/game_list.html'

    def get_context_data(self, **kwargs):
        print("hello" + str(kwargs))
        print(self.kwargs['pk'])
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user)
        print(current_coach)
        team_id = self.kwargs['pk']
        team = Team.objects.get(team_id = team_id)
        queryset = Game.objects.filter(team=team)
        print(queryset)
        return queryset

@method_decorator([login_required, coach_required], name='dispatch')
class TeamCreateView(CreateView):
    model = Team
    fields = ('name', )
    template_name = 'roster/coaches/team_add_form.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.coach_id = Coach.objects.get(user=self.request.user)
        team.save()
        messages.success(self.request, 'Go ahead and add players to your team now!')
        return redirect('coaches:team_change', team.pk)

@login_required
@coach_required
def player_add(request, pk):
    team = get_object_or_404(Team, pk=pk)

    if request.method == 'POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.team = team
            player.save()
            messages.success(request, 'You successfully created a player')
            return redirect('coaches:team_change', team.pk)
    else:
        form = PlayerForm()

    return render(request, 'roster/coaches/player_add_form.html', {'team': team, 'form': form})

@login_required
@coach_required
def player_change(request, team_pk, player_pk):
    team = Team.objects.get(pk = team_pk)
    player = get_object_or_404(Player, pk=player_pk, team=team)

    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            messages.success(request, 'Player saved with success!')
            return redirect('coaches:team_change', team.pk)
    else:
        form = PlayerForm(instance=player)

    return render(request, 'roster/coaches/player_change_form.html', {
        'team': team,
        'player': player,
        'form': form,
    })

@login_required
@coach_required
def game_add(request, pk):
    team = get_object_or_404(Team, pk=pk)

    if request.method == 'POST':
        form=GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.team = team
            game.save()
            messages.success(request, 'You successfully created a game')
            return redirect('coaches:schedule', team.pk)
    else:
        form = GameForm()

    return render(request, 'roster/coaches/game_add_form.html', {'team': team, 'form': form})

@login_required
@coach_required
def game_change(request, team_pk, game_pk):
    team = Team.objects.get(pk = team_pk)
    game = get_object_or_404(Game, pk=game_pk, team=team)

    if request.method == 'POST':
        form = GameForm(request.POST, instance=player)
        if form.is_valid():
            with transaction.atomic():
                form.save()
            messages.success(request, 'Game saved with success!')
            return redirect('coaches:schedule', team.pk)
    else:
        form = GameForm(instance=game)

    return render(request, 'roster/coaches/game_change_form.html', {
        'team': team,
        'game': game,
        'form': form,
    })



def real_time_tracker(request, team_pk):
    return render(request, 'roster/coaches/real_time_tracker.html')




