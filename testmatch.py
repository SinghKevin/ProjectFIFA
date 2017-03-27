from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D,SoccerState, SoccerAction
from soccersimulator import settings
import math
from strategy import * 

#class Observer(object):
# MAX_STEP=50
# def __init__(self,simu):
# self.simu = simu
# self.simu.listeners += self
# #ajout de lobserver
# def begin_match(self,team1,team2,state):
# #initialisation des parametres ...
# self.last, self.cpt, self.cpt_tot = 0, 0, 0,
# def begin_round(self,team1,team2,state):
# self.simu.state.states[(1,0)].position = Vector2D(130,45)
# self.simu.state.ball.position = Vector2D(130,45)
# self.last = self.simu.step
# def update_round(self,team1,team2,state):
# if self.simu.step>self.last+self.MAX_STEP:
# self.simu.end_round()
# def end_round(self,team1,team2,state):
# if state.goal>0:
# self.cpt+=1
# self.cpt_tot+=1
# self.res= self.cpt*1./self.cpt_tot
# print(self.res)
## if self.simu.step == self.MAX_STEP: #fin de la simu
## print(self.res)
## self.simu.end_match()

        
#Classe avec la memoire ==> A modifier
#class FonceurStrategy(Strategy):
#    def __init__(self):
#      Strategy.__init__(self,"Fonceur")
#      self.memoire = dict()
#      self.memoire[""a""] = 1
#    def compute_strategy(self,state,id_team,id_player):        
#       m_pos = toolbox_Action.Position(state, id_team, id_player)
#       m_action= toolbox_Action.Action(m_pos,self.memoire )
#        
#       return m_action.aller(m_pos.ball_position()) + m_action.shoot(m_pos.position_but_adv())        
        
        
        
        #return fonceur(Action(state, id_team, id_player))
#Stategie de defense
#class DefenseStrategy(Strategy):
#    def __init__(self):
#        Strategy.__init__(self,"Defense")
#    def compute_strategy(self, state, id_team, id_player):
#            return defense(Action(state, id_team, id_player))
       


#def dribble(m_action):
#    return m_action.dribbler()
#    
#def attaque(m_action):
#    return m_action.attaque()
#    
#def defense(m_action):
#     if Position.state.ball.position.x > 110:
#            return SoccerAction(Position.ball_position() - Position.my_position(),Vector2D(-50, 0))
#Stategie de defense

        




## Creation d'une equipe

team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")



team1.add("BG", MilieuStrategy())
#team1.add("Mertesacker",RandomStrategy()) #Strategie qui ne fait rien
team1.add("Alexis",CampeurStrategy_1())
#team1.add("Alexis",CampeurStrategy())

#team1 .add("Mertesacker",AttaqueStrategy()) #Strategie qui ne fait rien
team1.add("Campeur", GardienStrategy())  
team1.add("Samy-zer", CampeurStrategy())
#
team2.add("Pique",CampeurStrategy_1())   #Strategie aleatoire
#team2.add("Neymar", CampeurStrategy())
#team2.add("Campeur", Pos_Strategy())
#team2.add("Bakambu", Milieu_bas_Strategy())
team2.add("Pique",MilieuStrategy())   #Strategie aleatoire
team2.add("Neymar",CampeurStrategy())
team2.add("Campeur", GardienStrategy()) 
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)
#Jouer sans afficher
simu.start()

