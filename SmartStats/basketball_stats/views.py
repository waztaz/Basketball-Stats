from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the basketballstats index")

def basketballstats(request, player_id, game_id):
    response="You're looking at the stats for player {0} in game {0}."
    return HttpResponse(response.format(player_id, game_id))

def analytics(request, player_id):
	response="You're looking at analytics for player {0}."
    return HttpResponse(response.format(player_id))
