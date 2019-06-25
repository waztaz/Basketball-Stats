from django.test import TestCase
from myapp.models import Coach, Team, Player, Scout, Game, CumulativeStats, BasketballStats

# Create your tests here.
class CoachTestCase(TestCase):
	def setUp(self):
		Coach.objects.create(first_name="Test" , last_name="Coach")

	def test_coach_exists(self):
		"Testing for properly generated coach"
		#coach = Coach.objects.get()

class TeamTestCase(TestCase):
	def setUp(self):
		Team.objects.create(name="Cavaliers")

	#def test_coach_exists(self):


class PlayerTestCase(TestCase):
	def setUp(self):
		Player.objects.create(team="Cavaliers", first_name="Test", last_name="Player", height=68, weight=190, position=SG)

class ScoutTestCase(TestCase):
	def setUp(self):
		Scout.objects.create(first_name="Test" , last_name="Scout")

#class GameTestCase(TestCase):
#	def setUp(self):
#		Game.objects.create(first_name="Test" , last_name="Coach")

#class CumulativeStatsTestCase(TestCase):
#	def setUp(self):

#class BasketballStatTestCase(TestCase):
#	def setUp(self):
