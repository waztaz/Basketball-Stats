
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

from ..models import User, Coach, Team, Player
from ..forms import CoachSignUpForm

class CoachSignUpView(CreateView):
    model = User
    form_class = CoachSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'coach'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('coaches:team_list')


#@method_decorator([login_required, teacher_required], name='dispatch')
class TeamListView(ListView):
    model = Team
    ordering = ('team_name', )
    #context_object_name = 'team'
    template_name = 'roster/coaches/team_list.html'

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user)
        print(current_coach)
        queryset = Team.objects.filter(coach_id=current_coach)
        print(queryset)
        return queryset

class PlayerListView(ListView):
    model = Player
    ordering = ('first_name', 'last_name', )
    template_name = 'roster/coaches/team_change_form.html'

    def get_queryset(self):
        queryset=Player.objects.filter(team=self.kwargs.get('pk'))
        print(queryset)
        return queryset




class TeamUpdateView(UpdateView):
    model=Team
    fields = ('team_name', 'coach_id', )
    template_name = 'roster/coaches/team_change_form.html'

    def get_context_data(self, **kwargs):
        kwargs['players'] = self.get_object().players
        #kwargs['team'] = self.get_object().team_name
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user)
        print(current_coach)
        queryset = Team.objects.filter(coach_id=current_coach)
        print(queryset)
        return queryset

    def get_success_url(self):
        return reverse('coaches:team_change', kwargs={'pk': self.object.pk})

class TeamCreateView(CreateView):
    model = Team
    fields = ('name', )
    template_name = 'classroom/teachers/team_add_form.html'

    def form_valid(self, form):
        team = form.save(commit=False)
        team.coach_id = self.request.user
        team.save()
        messages.success(self.request, 'Go ahead and add players to your team now!')
        return redirect('coaches:team_change', team.pk)

