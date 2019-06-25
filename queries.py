from roster.models import *

'''
SELECT player_id, team_score, opponent_score, game_id
FROM LineupScore
INNER JOIN LineupPlayer
ON lineup_id = lineup_id
'''
def queryPlayerPlusMinus(player_id):
    LineupPlayer.objects.filter(player_id = player_id).select_related(
            lineup_id, 
            player_id,
            game_id,
            team_score,
            opponent_score)


def getPlayersFromTeam(team_id):
    Player.objects.filter(team_id = team_id)

def getTeamGames(team_id):
    Game.objects.filter(team_id = team_id)

def getPlayersByYear(team_id, year_in_school):
    Player.objects.filter(year_in_school = year_in_school)

def getPlayersByPosition(team_id, position):
    Player.objects.filter(position = position)

