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
        s.add("Iniesta", AttaqueStrategy() )
    if i == 2:
        s.add("Yaya",GardienStrategy()  )
        s.add("Zlatan",AttaqueStrategy() )
    if i ==4 :
        s.add("Aguero",AttaqueStrategy() )
        s.add("Suarez ",AttaqueStrategy() )
        s.add("Puyol ", GardienStrategy() )
        s.add("T. Silva", GardienStrategy())
    
    return s
