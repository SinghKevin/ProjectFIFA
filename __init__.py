#from teams import team1, team2
from soccersimulator import Player,SoccerTeam
from strategy import *
##Creation d'une equipe
#team1 = SoccerTeam(name="team1",login="etu1")
#team2 = SoccerTeam(name="team2",login="etu2")
#
##Choix de Strat
#team1.add("Neymar",AttaqueStrategy())
#team2.add("Alexis",AttaqueStrategy())
#team2.add("Silva",DefenseStrategy())


def get_team(i):
    s= SoccerTeam(name = "TeamFUT")
    if i == 1:
        s.add("Iniesta", AttaqueStrategy())
    if i == 2:
        s.add("Yaya",GardienStrategy())
        s.add("Zlatan",CampeurStrategy())
    if i ==4 :
	s.add("BG", MilieuStrategy())
	s.add("Alexis",CampeurStrategy_1())
	s.add("Campeur", GardienStrategy())  
	s.add("Samy-zer", CampeurStrategy())
    
    return s
