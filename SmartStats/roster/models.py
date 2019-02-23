from django.db import models
from enum import Enum

# Create your models here.

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

