from django.db import models
from enum import Enum
from django.contrib.auth.models import User

# Create your models here.

class Coach(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, default='Coach')
    coach_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name_text

class Team(models.Model):
    team_id=models.AutoField(primary_key=True)
    coach_id=models.ForeignKey(Coach, on_delete=models.CASCADE)
    team_name=models.CharField(max_length=100)

    def __str__(self):
        return self.team_name_text

class PlayerPosition(Enum):
    PG="Point Guard"
    SG="Shooting Guard"
    SF="Small Forward"
    PF="Power Forward"
    C="Center"


class YearInSchool(Enum):
    FR="Freshman"
    SO="Sophomore"
    JR="Junior"
    SR="Senior"

class Player(models.Model):
    player_id=models.AutoField(primary_key=True)
    team_id=models.ForeignKey(Team, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    #height in inches
    height=models.IntegerField(default=0)
    #weight in lbs
    weight=models.IntegerField(default=0)
    position=models.CharField(
            max_length=2,
            choices=[(tag, tag.name) for tag in PlayerPosition]
            )
    year_in_school=models.CharField(
            max_length=2,
            choices=[(tag, tag.name) for tag in YearInSchool]
            )

<<<<<<< HEAD
#class Scout(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
=======
    def __str__(self):
        return self.first_name_text


class Scout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
>>>>>>> url_models_veijay

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
<<<<<<< HEAD
class LineupPlayer(models.Model):
    lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE, related_name="lineup")
    player_id = models.ForeignKey(Lineup, on_delete = models.CASCADE, related_name="player")
=======
#class LineupPlayer(models.Model):
 #   lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
  #  player_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
>>>>>>> url_models_veijay

class LineupScore(models.Model):
    lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
    time_stamp_entered = models.DateTimeField()
    time_stamp_left = models.DateTimeField()
    team_score = models.IntegerField()
    opponent_score = models.IntegerField()
