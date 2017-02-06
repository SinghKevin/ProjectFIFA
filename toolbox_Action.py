# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:54:40 2017

@author: 3202238
"""



from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#Toolbox
class Position(object):
    def __init__(self, state, id_team, id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
    
    def my_position(self):
        return self.state.player_state(self.id_team, self.id_player).position
    
    def ball_position(self):
        return self.state.ball.position
    def ball_positionX(self):
        return self.state.ball.position.x
    def ball_positionY(self):
        return self.state.ball.position.y

    def position_but_adv(self):
        if self.id_team == 1:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        
        
#####################################################################################################
        
class Action(object) :
    def __init__(self, state):
        self.state = state
#        self.id_team = id_team
#        self.id_player = id_player
#        self.mon_but = Vector2D(0, settings.GAME_HEIGHT/2)
#        self.but_adv = Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT/2)
#        self.Position = Position
    def aller(self, p):
        return SoccerAction(p-self.state.my_position(), Vector2D())
        
    def shoot(self, p):
        return SoccerAction(Vector2D(), p-self.state.my_position())
    def mini_shoot(self, p):
        return SoccerAction(Vector2D(), (p-self.state.my_position())*0.02)
        
            
    def dribbler(self):
        if (self.state.id_team == 1):
            
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX() >100:
                return self.shoot(self.state.position_but_adv())
            else:
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())
        else: 
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX() <50:
                return self.shoot(self.state.position_but_adv())
            else:
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())

    def defense(self):
        if (self.state.id_team ==1):
            if self.state.ball_positionX() < 40 :
                return self.aller(self.state.ball_position()) + self.shoot(Vector2D(50, 0))
        
        else:
            if self.state.ball_positionX() > 110 :
                return self.aller(self.state.ball_position()) + self.shoot(Vector2D(-50, 0))
#    def dribbler(self):
#        if (self.state.ball_position()-self.state.my_position()) <= Vector2D(settings.PLAYER_RADIUS + settings.BALL_RADIUS,settings.PLAYER_RADIUS + settings.BALL_RADIUS) and self.state.ball_positionX() >110:
#            return self.shoot(self.state.position_but_adv())
#        else:
#            return self.aller(self.state.ball_position())+self.shoot(self.state.my_position()+Vector2D(1,0))


#    def dribbler(self,id_team, id_player):
 #       if self.ball_position() < 130:
  #          return shoot(1,0)
#    def dribbler(self):
 #       if self.state.ball.position.x>110:
  #          return self.shoot(self.but_adv)
   #     else: