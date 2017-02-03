import toolbox_Action
#from teams import team1, team2
from soccersimulator import Player,SoccerTeam
from strategy import AttaqueStrategy,DefenseStrategy
#Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")

#Choix de Strat
team1.add("Neymar",AttaqueStrategy())
team2.add("Alexis",AttaqueStrategy())
team2.add("Silva",DefenseStrategy())
