from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D,SoccerState, SoccerAction
from soccersimulator import settings
import math
from strategy import * 

        
## Creation d'une equipe

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")



team1.add("BG", MilieuStrategy())
team1.add("Alexis",CampeurStrategy_1())
team1.add("Campeur", GardienStrategy())  
team1.add("Samy-zer", CampeurStrategy())

team2.add("Pique",CampeurStrategy_1())
team2.add("Pique",MilieuStrategy())
team2.add("Neymar",CampeurStrategy())
team2.add("Campeur", GardienStrategy()) 
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()

