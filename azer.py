# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:28:02 2017

@author: singh
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:31:09 2017
@author: 3520543
"""


from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math

class MyState(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.idteam=idteam
        self.idplayer= idplayer
        self.key = (idteam,idplayer)
    def my_position(self):
        return self.state.player_state(self.key[0], self.key[1]).position
        #equivalent a self.player_state(self.key[0],self.key[1])
    def ball_position(self):
        return self.state.ball.position
   
    def ball_vitesse(self):
        return self.state.ball.vitesse
        
    # début des modifications
    def ball_positionX(self):
        return self.state.ball.position.x
        
    def ball_positionY(self):
        return self.state.ball.position.y
        
    def position_but_adv(self):
        if self.idteam == 1:
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        
    def ball_position_future(self):
        if self.ball_vitesse().norm > 1 or self.ball_vitesse().norm < -1:
            return self.ball_position()+self.ball_vitesse()*10
        else :
            return self.ball_position()
        
    def position_coop_proche_team(self):
        pos=self.position_but_adv()
        if self.idteam ==1 :
            for (it,ip) in self.state.players:
                if it == 1 and ip != self.idplayer:
                    if self.state.players[it,ip].position().norm() <pos.norm():
                        pos=(it,ip).my_position()
            return pos
    
    


class MyAction(object):
    def __init__(self,state):
        self.state = state
#    def __getattr__(self, name):
#        return getattr(self.state, name)
    
    def aller(self,p):
        return SoccerAction((p-self.state.my_position()),Vector2D())
    
    def aller_vers_balle(self):
        return self.aller(self.state.ball_position()+self.state.ball_vitesse()*5)
    
    def shoot(self,p):
        return SoccerAction(Vector2D(0,0),0.1*(p-self.state.my_position()))
    
    def shoot_but(self):
        if (self.state.ball_position()-self.state.my_position()).norm <=settings.PLAYER_RADIUS + settings.BALL_RADIUS:
        	return self.shoot(self.state.position_but_adv())
        else :
        	return self.aller_vers_balle()
	
    def pousse_ball(self):
        if (self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            return SoccerAction(Vector2D(),(self.state.position_but_adv() - self.state.ball_position())*0.02)
        else :
            return self.aller_vers_balle()
	
 
 
    def pousse_ball_centre(self):
        if (self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS:
            if self.state.idteam==1:                
                if self.state.ball_positionX()<75:
                    return SoccerAction(Vector2D(),(Vector2D(1,-2)))
                else :
                    return SoccerAction(Vector2D(),(Vector2D(1,2)))
            else: 
                if self.state.ball_positionX()<75:
                    return SoccerAction(Vector2D(),(Vector2D(-1,-2)))
                else :
                    return SoccerAction(Vector2D(),(Vector2D(-1,2)))
        else :
            return self.aller_vers_balle()
#    def dribble_team1(self):
#        if (self.state.ball_position()-self.state.my_position() <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
#            return SoccerAction(Vector2D(),(self.state.position_but_adv() - self.state.ball_position())*0.01)
#        else : 
#             return self.aller_vers_balle()
#    def dribble_team2(self):
#             return self.aller_vers_balle()+SoccerAction(Vector2D(),Vector2D(-1,-0.2))
    
    def degagement(self): #p=position du dégagement
        return self.shoot_but()

    def passe(self):
        if self.state.idteam == 1:
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
                return self.shoot(Vector2D(85,45))
            else :
                return self.aller_vers_balle()
        else :
            if ((self.state.ball_position()-self.state.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS):
                return self.shoot(Vector2D(65,45))
            else :
                return self.aller_vers_balle()

    def action_attaquant(self):
        if self.state.idteam==1:
            if ((self.state.ball_positionX()>60 and self.state.ball_positionX()<90) and (self.state.ball_positionY()<60 and self.state.ball_positionY()>30) ):
                return self.pousse_ball_centre()         
            elif ((self.state.ball_positionX()<settings.GAME_WIDTH-40)):
                return self.pousse_ball()
            else : 
                return self.shoot_but()
        else :
             if ((self.state.ball_positionX()>60 and self.state.ball_positionX()<90) and (self.state.ball_positionY()<60 and self.state.ball_positionY()>30) ):
                return self.pousse_ball_centre()            
             elif self.state.ball_positionX()>settings.GAME_WIDTH-110:
                return self.pousse_ball()
             else :
                return self.shoot_but()            

    def action_gardien(self):
        if self.state.idteam==1:
            if self.state.ball_positionX()>settings.GAME_WIDTH-110:
                if self.state.ball_positionY()>30 and self.state.ball_positionY()<60:                    
                    return self.aller(Vector2D(15,self.state.ball_position_future().y))
                else :
                    return self.aller(Vector2D(15,45))
                #return self.aller(Vector2D(25,45))
            else:
                return self.degagement()
        else:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                if self.state.ball_positionY()>30 and self.state.ball_positionY()<60:
                    return self.aller(Vector2D(135,self.state.ball_position_future().y))
                else :
                    return self.aller(Vector2D(135,45))#
            else:
                return self.degagement()
              
    def action_def(self):
        if self.state.idteam==1:
            if self.state.ball_positionX()<80:
                return self.passe()
            else : 
                 return self.aller(Vector2D(25,45))
        else :
            if self.state.ball_positionX()>70:
                return self.passe()
            else :
                return self.aller(Vector2D(125,45))
    def action_milieu(self):
        if self.state.idteam==1:
            if self.state.ball_positionX()<85:
                return self.passe()
            else : 
                 return self.aller(Vector2D(45,45))
        else :
            if self.state.ball_positionX()>65:
                return self.passe()
            else :
                return self.aller(Vector2D(105,45))
    def action_attaquant4(self):
        if self.state.idteam==1:
            if ((self.state.ball_positionX()<75)):
                return self.aller(Vector2D(80,45))
            elif self.state.ball_positionX()<110 :
                return self.pousse_ball()
            else : 
                return self.shoot_but()
        else :
            if ((self.state.ball_positionX()>75)):
                return self.aller(Vector2D(70,45))
            elif self.state.ball_positionX()>40 :
                return self.pousse_ball()
            else : 
                return self.shoot_but()