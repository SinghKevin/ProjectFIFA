# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:20:48 2017

@author: 3202238
"""

#Toolbox Attaque

class Toolbox (object):
        def __init__self(self, state, idteam, idplayer):
            self.state = state
            self.idt = idteam
            self.idp = idplayer
            
        def position (self):
            return state.player_state(idt,idp)
            
            
        def deplacement(self,p):
            return SoccerAction(p-self.my_position(), Vector2D() )
            
        def tir (self, p):
            return SoccerAction(Vector2D(), p-self.state.my_position() )
            
        #def calcul_angle(self, norme, angle):
            
             