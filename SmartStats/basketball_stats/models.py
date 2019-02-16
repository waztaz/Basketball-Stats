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
class Game(model.Models):
	game_id= models.AutoField(primary_key = True)
	team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
	opponent = models.CharField(max_length = 30)	#TODO: other team might not be using SmartStats?
	location = models.CharField(max_length = 100)

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

class Play(model.Models):
	team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
	play_num = models.IntegerField()
	position = models.CharField(max_length = 100) #TODO: might refer to player position
	action = models.CharField(max_length = 100)
	sequence = models.IntegerField()

class Lineups(model.Models):
	game_id = models.ForeignKey(Game, on_delete = models.CASCADE)
	time_stamp_1 = models.DateTimeField()
	time_stamp_2 = models.DateTimeField()
	

