# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:15:23 2017

@author: 3202238
"""

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
        return m_action.aller(m_pos.ball_position()) + m_action.shoot(m_pos.position_but_adv())
        
class DefenseStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.defense()

class GardienStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.gardien() 

class AttaqueStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self, "ronaldinho")
    def compute_strategy(self, state, id_team, id_player):
        m_pos = test_bis.Position(state, id_team, id_player)
        m_action= test_bis.Action(m_pos)
        return m_action.dribbler()