import golf
#from teams import team1, team2
from soccersimulator import Player,SoccerTeam
from strategy import AttaqueStrategy,DefenseStrategy

team1 = SoccerTeam() 
team2 = SoccerTeam() 

def get_slalom_team1():
    team1.add("John",Golfeur_slalom())
    return team1

def get_slalom_team2():
    team1.add("John",Golfeur_slalom())
    return team2
    
def get_golf_team1():
    team1.add("John",Golfeur_golf())
    return team1

