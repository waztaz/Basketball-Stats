from django.db import models

#Defining Classes for SmartStats

#Copied over from VJ's branch, will determine how to fix merge conflicts/split up by Feb. 22 commit
class Coach(models.Model):

    coach_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)

    last_name=models.CharField(max_length=50)

class Team(models.Model):

    team_id=models.AutoField(primary_key=True)

    coach_id=models.ForeignKey(Coach, on_delete=models.CASCADE)

    team_name=models.CharField(max_length=100)

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

class Stat(Enum):
    2_point_make 
    2_point_miss
    3_point_make
    3_point_miss
    free_throw_make
    free_throw_miss
    assist
    rebound
    turnover
    steal
    block

class Player(models.Model):

    player_id=models.AutoField(primary_key=True)

    team_id=models.ForeignKey(Team, on_delete=models.CASCADE)

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



#Original Classes
class Game(models.Models):
    game_id= models.AutoField(primary_key = True)
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    opponent = models.CharField(max_length = 100)        #TODO: other team might not be using SmartStats?
    location = models.CharField(max_length = 100)
    team_score = models.IntegerField(default = 0)
    opponent_score = models.IntegerField(default = 0)

class Analytics(model.Models):
	player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
	#TODO: link to actual stats and add functions

class BasketballStat(model.Models):
    player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
    time_stamp = models.DateTimeField()
    stat = models.CharField(max_length = 30)
    shot_location = models.IntegerField()

#TODO: class Stat(model.Models):
#Stretch goal for other sports

#represents a play
class Play(model.Models):
	team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
	play_num = models.IntegerField()
	position = models.CharField(max_length = 100) #TODO: might refer to player position
	action = models.CharField(max_length = 100)
	sequence = models.IntegerField()

#represents a lineup
class Lineup(model.Models):
    point_guard = models.ForeignKey(Player, on_delete = models.CASCADE)
    shooting_guard = models.ForeignKey(Player, on_delete = models.CASCADE)
    small_forward = models.ForeignKey(Player, on_delete = models.CACADE)
    power_forward = models.ForeignKey(Player, on_delete = models.CASCADE)
    center = models.ForeignKey(Player, on_delete = models.CASCADE)

#represents a player in a lineup
class PlayerLineup(models.Model):
    player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
    lineup - models.ForeignKey(Lineup, on_delete = models.CASCADE)

#represents a Lineup's stats in a time period
class LineupScore(model.Models):
    game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
    lineup_id = models.ForeignKey(Lineup, on_delete = models.CASCADE)
    time_stamp_entered = models.DateTimeField()
    time_stamp_left = models.DateTimeField()
    team_score_entered = models.IntegerField()
    opponent_score_entered = models.IntegerField()
    team_score_left = models.IntegerField()
    opponent_score_entered = models.IntegerField()

class Stats(models.Model):
    game_id = models.DateTimeField()
    timestamp = models.DateTimeField()
    player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
    stat=models.CharField(
            max_length=15,
            choices=[(tag, tag.name) for tag in Stat]
            )
 

    

