from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator import Vector2D,SoccerState, SoccerAction
from soccersimulator import settings
import math
import test_bis

class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction(Vector2D.create_random(-1,1),Vector2D.create_random(-1,1))
        

#def fonceur(m_action):
#     return m_action.aller(m_pos.ball_position()) + m_action.shoot(m_pos.position_but_adv())
     
     ## Strategie d'attaque

        
class FonceurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):        
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.aller(m_pos.ball_position())
        
class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.defense()

class GardienStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Gardien")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.gardien() 

class AttaqueStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "Attaque")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.dribbler()


class CampeurStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.attaque_2vs2()

class CampeurStrategy_1(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.attaque_2vs2_bis()


class AttaqueStrategy_1vs1(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.defenseur_1vs1()

class Pos_Strategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.aller(Vector2D(75,65))
        
class DribbleStrategy(Strategy):
    def __ini__(self):
        Strategy.__init__(self,"Dribble")
    def compute_strategy(self,state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.dribbler_2()
        
#class ShooteurStrategy(Strategy):
#    def __init__(self):        
#        Strategy.__init__(self,"Fonceur")
#    def compute_strategy(self,state,id_team,id_player):
#        m_pos = test_bis.Position(state, id_team, id_player)
#        m_action= test_bis.Action(m_pos)
#        return m_action.shooteur_2()
        
class ShooteurStrategy(Strategy):
    def __init__(self):        
        Strategy.__init__(self,"Fonceur")
    def compute_strategy(self,state,id_team,id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.dribbler_2() + m_action.shoot(m_pos.position_but_adv())

class MilieuStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Passeur")
    def compute_strategy(self,state,id_team, id_player):
        m_pos = test_bis.Position(state,id_team,id_player)
        m_action = test_bis.Action(m_pos)
        return m_action.milieu()

