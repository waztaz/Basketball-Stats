from django.db import models
from enum import Enum
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.utils.html import escape, mark_safe

DEFAULT_USER = 'default_user'
DEFAULT_TEAM = 'default_team'

# Create your models here.

#Creating Custom User

class User(AbstractUser):
    is_player=models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)



def get_default_user():
    return User.objects.get_or_create(username=DEFAULT_USER)[0].pk

def get_default_team():
    return Team.objects.get_or_create(name=DEFAULT_TEAM)[0]

def get_default_coach():
    return Coach.objects.get_or_create(user=get_default_user())[0]

class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user())
    coach_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, default="coach")
    last_name=models.CharField(max_length=50, default="coach")
    
    #def __str__(self):
        #return self.first_name.text

class Team(models.Model):
    team_id=models.AutoField(primary_key=True)
    coach_id=models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='teams')
    name=models.CharField(max_length=100)

    #def __str__(self):
        #return self.name.text

class PlayerPosition(Enum):
    PG="Point Guard"
    SG="Shooting Guard"
    SF="Small Forward"
    PF="Power Forward"
    C="Center"

    #def __str__(self):
        #return self.name.text

class PlayerPosition(Enum):
    PG="Point Guard"
    SG="Shooting Guard"
    SF="Small Forward"
    PF="Power Forward"
    C="Center"

"""
class PlayerPosition(Enum):
    (PG, "Point Guard")
    (SG, "Shooting Guard")
    (SF, "Small Forward")
    (PF, "Power Forward")
    (C, "Center")
"""

class YearInSchool(Enum):
    FR="Freshman"
    SO="Sophomore"
    JR="Junior"
    SR="Senior"

class Player(models.Model):
    POINT_GUARD = 'PG'
    SHOOTING_GUARD = 'SG'
    SMALL_FORWARD = 'SF'
    POWER_FORWARD = 'PF'
    CENTER = 'C'
    PLAYER_POSITION_CHOICES = (
        (POINT_GUARD, "Point Guard"),
        (SHOOTING_GUARD, "Shooting Guard"),
        (SMALL_FORWARD, "Small Forward"),
        (POWER_FORWARD, "Power Forward"),
        (CENTER, "Center"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user())
    player_id=models.AutoField(primary_key=True)
    team=models.ForeignKey(Team, on_delete=models.CASCADE, null=True, related_name='players')
    first_name=models.CharField(max_length=100, default= "no name")
    last_name=models.CharField(max_length=100, default="no name")
    #height in inches
    height=models.IntegerField(default=0)
    #weight in lbs
    weight=models.IntegerField(default=0)
    position=models.CharField(
            max_length=2,
            choices=PLAYER_POSITION_CHOICES,#[(tag, tag.name) for tag in PlayerPosition],
            #null=True
            default=CENTER,
    )
    """
    year_in_school=models.CharField(
            max_length=2,
            choices=[(tag, tag.name) for tag in YearInSchool],
            )
    """
#class Scout(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)


    def __str__(self):
        return self.first_name_text


class Scout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

"""
########################## TO BE MOVED TO OWN APP LATER ###################
class Game(models.Model):
    game_id= models.AutoField(primary_key = True)
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    opponent = models.CharField(max_length = 100)        #TODO: other team might not be using SmartStats?
    location = models.CharField(max_length = 100)
    team_score = models.IntegerField(default = 0)
    opponent_score = models.IntegerField(default = 0)

class Analytics(models.Model):
        player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
        #TODO: link to actual stats and add functions

class BasketballStat(models.Model):
    player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
    time_stamp = models.DateTimeField()
    stat = models.CharField(max_length = 30)
    shot_location = models.IntegerField()

class Play(models.Model):
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    play_num = models.IntegerField()
    position = models.CharField(max_length = 100) #TODO: might refer to player position
    action = models.CharField(max_length = 100)
    sequence = models.IntegerField()
    screen_for = models.CharField(max_length = 100)


#represents a single Lineup on the court
class Lineup(models.Model):
    lineup_id = models.AutoField(primary_key = True)
    point_guard = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="point_guard")
    shooting_guard = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="shooting_guard")
    small_forward = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="small_forward")
    power_forward = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="power_forward")
    center = models.ForeignKey(Player, on_delete = models.CASCADE, related_name="center")

#Many players in many lineups so need to create this

class LineupPlayer(models.Model):
    lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE, related_name="lineup")
    player_id = models.ForeignKey(Lineup, on_delete = models.CASCADE, related_name="player")

#class LineupPlayer(models.Model):
 #   lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
  #  player_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)



class LineupScore(models.Model):
    lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
    time_stamp_entered = models.DateTimeField()
    time_stamp_left = models.DateTimeField()
    team_score = models.IntegerField()
    opponent_score = models.IntegerField()


"""
