
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

from ..models import User, Coach, Team
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
        return redirect('coaches:team_change_list')

#@method_decorator([login_required, teacher_required], name='dispatch')
class TeamListView(ListView):
    model = Team
    ordering = ('team_name', )
    context_object_name = 'teams'
    template_name = 'roster/coaches/team_change_list.html'

    def get_queryset(self):
        current_coach = Coach.objects.get(user=self.request.user).pk
        queryset = Team.objects.filter(coach_id = current_coach)
        return queryset
