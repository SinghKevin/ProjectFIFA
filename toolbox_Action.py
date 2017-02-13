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
            
    def ball_vitesse(self):
        return self.state.ball.vitesse
    
    def zone_tir(self):
        return (self.ball_position()-self.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS
#    
#    def pos_j1(self):
#         return self.state.player_state(self.id_team,1).position
#         
#    def pos_j2(self):
#         return self.state.player_state(self.id_team,2).position        

    
    def ball_trajectoire(self):
        return self.ball_position() + self.ball_vitesse()*11
    
    def ball_trajectoire_gardien(self):
        return self.ball_position() + self.ball_vitesse()*12         
        
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
        return SoccerAction((p-self.state.my_position()), Vector2D())    
    
    def aller_balle(self):
        return self.aller(self.state.ball_trajectoire())
        
    def shoot(self, p):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1)
    
    def degagement(self):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(),self.state.position_but_adv()-self.state.my_position())
        else :
            return self.aller(self.state.ball_position())
        
    def mini_shoot(self, p):
        if self.state.zone_tir() :
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.015)
        else :
            return self.aller(self.state.ball_position())
            
#    def passe(self):
#        if (self.state.id_player == 1):
#                return self.shoot(self.state.pos_j2())
#        else :
#            return self.shoot(self.state.pos_j1())
    

    
#    def placement_gardien(self):
#        return self.aller(Vector2D(10,self.state.ball_position()+self.state.vitesse_balle()*11 ))
        
#    def passe(self):
#        if (self.state.id_player == 1):
#                return self.shoot(self.state.pos_j2())
#        else :
#            return self.shoot(self.state.pos_j1())
        
    def gardien1(self):
        if self.state.id_team==1:
            if self.state.ball_positionX()>settings.GAME_WIDTH-110:
                if self.state.ball_positionY()>30 and self.state.ball_positionY()<60:                    
                    return self.aller(Vector2D(15,self.state.ball_trajectoire_gardien().y))
                else :
                    return self.aller(Vector2D(15,45))
    
            else:
                return self.degagement()
        else:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                if self.state.ball_positionY()>30 and self.state.ball_positionY()<60:
                    return self.aller(Vector2D(135,self.state.ball_trajectoire_gardien().y))
                else :
                    return self.aller(Vector2D(135,45))
            else:
                return self.degagement()
    
    def gardien_haut(self):
        if self.state.id_team==1:
            if self.state.ball_positionX()>settings.GAME_WIDTH-90:
                if self.state.ball_positionY()>50 and self.state.ball_positionX()<75:                    
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(10,50))
               
            else:
                return self.degagement()
        else:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                if self.state.ball_positionY()>50 and self.state.ball_positionY()>75:
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(135,50))
            else:
                return self.degagement()
    def gardien_bas(self):
        if self.state.id_team==1:
            if self.state.ball_positionX()>settings.GAME_WIDTH-90:
                if self.state.ball_positionY()<40 and self.state.ball_positionX()<75:                    
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(10,40))
   
            else:
                return self.degagement()
        else:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                if self.state.ball_positionY()<40 and self.state.ball_positionY()>75:
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(135,40))
            else:
                return self.degagement()
    def gardien_milieu(self):
        if self.state.id_team==1:
            if self.state.ball_positionX()>settings.GAME_WIDTH-90:
                if self.state.ball_positionY()>40 and self.state.ball_positionY()<50 and self.state.ball_positionX()<75:                    
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(10,45))

            else:
                return self.degagement()
        else:
            if self.state.ball_positionX()<settings.GAME_WIDTH-40:
                if self.state.ball_positionY()>40 and self.state.ball_positionY()<50 and self.state.ball_positionY()>75:
                    return self.aller(self.state.ball_trajectoire_gardien())
                else :
                    return self.aller(Vector2D(135,45))
            else:
                return self.degagement()
                
    def gardien(self):
        if self.state.ball_positionY()>50:
            return self.gardien_haut()
        elif self.state.ball_positionY()<40:
            return self.gardien_bas()
        else:
            return self.gardien_milieu()

            
        
            
    def dribbler(self):
        if (self.state.id_team == 1):
            if self.state.zone_tir() and self.state.ball_positionX() >110:
                return self.shoot(self.state.position_but_adv())    
                
            elif self.state.zone_tir():       
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())
                
            else:
                return self.aller(self.state.ball_position())
                
        else: 
            if self.state.zone_tir() and self.state.ball_positionX() <40:
                return self.shoot(self.state.position_but_adv())
                
            elif self.state.zone_tir():       
                return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv())
                
            else:
                return self.aller(self.state.ball_position())
                
                
    def defense(self):
        if (self.state.id_team ==1):
            if self.state.zone_tir()  and self.state.ball_positionX()  < 75 : 
                return self.aller(self.state.ball_position()+self.state.ball_vitesse()*5) +self.shoot(self.state.position_but_adv())
                
            elif self.state.ball_positionX() < 75 :
                return self.aller(self.state.ball_position()+self.state.ball_vitesse()*5)    
        
        else:
            if self.state.zone_tir()  and self.state.ball_positionX()  > 100 : 
                return self.aller(self.state.ball_position()+self.state.ball_vitesse()*9) + self.shoot(self.state.position_but_adv())
                
            elif self.state.ball_positionX() > 100 :
                return self.aller(self.state.ball_position()+self.state.ball_vitesse()*9)   

                  
                
#    def gardien(self):
#        if (self.state.id_team ==1):
#            if (self.state.ball_positionX()>40) :
#                return  self.placement_gardien()
#            else :
#                if self.state.zone_tir()  :
#                    return self.aller(self.state.ball_position()+self.state.vitesse_balle()*150) +self.shoot(self.state.position_but_adv()) 

#    def dribble(self):
#        if 
                
#    def retourDef(self):
#        if 
#        return aller(Vector2D(50,50))        

            
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
   #     else