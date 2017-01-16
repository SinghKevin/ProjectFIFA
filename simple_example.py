from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D,SoccerState, SoccerAction
from soccersimulator import settings
import math

## Strategie aleatoire
class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))
        

## Strategie ToutDroit
class ToutDroitStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"ToutDroit")
    def compute_strategy(self,state,id_team,id_player):
         return SoccerAction(state.ball.position - state.player_state(id_team,id_player).position,Vector2D(1,0))
         

## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",ToutDroitStrategy() ) #Strategie qui ne fait rien
team2.add("Paul",RandomStrategy())   #Strategie aleatoire

#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()
