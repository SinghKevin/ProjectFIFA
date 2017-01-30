# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:20:48 2017

@author: 3202238
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#Toolbox

class Toolbox(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        self.mon_but = Vector2D(0, settings.GAME_HEIGHT/2)
        self.but_adv = Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    def ball_position(self):
        return self.state.ball.position

    def aller(self, p):
        return SoccerAction(p-self.my_position(), Vector2D())
        
    def shoot(self, p):
        return SoccerAction(Vector2D(), p-self.my_position())
        
#    def dribbler(self, p):
#        if ball_position() < 130:
#            return shoot(1,0)