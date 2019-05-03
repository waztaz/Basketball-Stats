
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_coach:
            return redirect('coaches:team_list')
        else:
            return redirect('players:player_home')
    return render(request, 'roster/home.html')

