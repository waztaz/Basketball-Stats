from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Roster homepage!")

def coach(request):
    return HttpResponse("Rosters for a particular coach")

def team(request):
    return HttpResponse("Roster page - list of players and information")

def player(request, team_id, player_id):
    response="You're looking at player {0} who plays for team {1}."
    return HttpResponse(response.format(player_id, team_id))
