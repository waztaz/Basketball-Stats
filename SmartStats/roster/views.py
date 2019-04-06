from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return HttpResponse("Roster homepage!")

#home page - home.html
def home(request):
    return render(request, 'roster/home.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created for %s' % (username))
			return redirect('home')
	else:
		form = UserRegisterForm()
	return render(request, 'roster/register.html', {'form': form})
	#return render_to_response('roster/register.html', RequestContext(request, {'form': form}))

def login(request):
	return render(request, 'roster/login.html')

def coach(request):
    return HttpResponse("Rosters for a particular coach")

def team(request):
    return HttpResponse("Roster page - list of players and information")

def player(request, team_id, player_id):
    response="You're looking at player {0} who plays for team {1}."
    return HttpResponse(response.format(player_id, team_id))
