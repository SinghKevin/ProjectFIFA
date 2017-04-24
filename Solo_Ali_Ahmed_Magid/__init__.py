#from teams import team1, team2
from soccersimulator import Player,SoccerTeam
from golf import Golfeur 
from golf import Slalom 

##Creation d'une equipe

def get_golf_team():
	team1 = SoccerTeam()
	team1.add("John",Golfeur())
	return team1

def get_slalom_team1():
	team1 = SoccerTeam()
	team1.add("John",Slalom())
	return team1
