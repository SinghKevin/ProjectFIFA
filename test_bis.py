from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#==============================================================================#
#                               #Toolbox                                       #
#==============================================================================#
class Position(object):
    def __init__(self, state,id_team,id_player):
        self.state = state
        self.id_team = id_team
        self.id_player = id_player
        self.key = (id_team, id_player)
    
    def my_position(self):
        return self.state.player_state(self.key[0],self.key[1]).position
    def get_coequipier(self):
        return list(reversed ([ (self.state.player_state(idt,idp).position.distance(self.my_position()),self.state.player_state(idt,idp).position)\
                for idt,idp in self.state.players if idt == self.id_team and  idp != self.id_player]))
    
    def get_ennemi(self):
        return list( reversed([ (self.states[(idt,idp)].position.distance(self.my_position()),self.states[(idt,idp)].position)\
                for idt,idp in self.states.keys() if idt != self.id_team]))      
        
        
    def pos_joueur_plus_proche(self): 
        L= self.get_coequipier()
        return L[0][1]

        
    
    def ball_position(self):
        return self.state.ball.position
        
    def ball_positionX(self):
        return self.state.ball.position.x
        
    def ball_positionY(self):
        return self.state.ball.position.y
        
    def ball_vitesse(self):
        return self.state.ball.vitesse
    
    def zone_tir(self):
        return (self.ball_position()-self.my_position()).norm <= settings.PLAYER_RADIUS + settings.BALL_RADIUS
    
    def ball_trajectoire(self):
        return (self.ball_position() + self.ball_vitesse()*20)
    
    def ball_trajectoire_gardien(self):
        return (self.ball_position() + self.ball_vitesse()*20)   
    
    def ball_trajectoire_milieu(self):
        return (self.ball_position() + self.ball_vitesse()*27)  
        
    def distance_but_ball_att(self):
        return abs(self.position_but_adv().x-self.ball_positionX())
        
    def distance_but_ball(self):
        return abs(self.position_mon_but().x-self.ball_positionX())
    
    def position_but_adv(self):
        if (self.key[0]==1):
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        
    def position_mon_but(self):
        if (self.key[0]==1):
            return Vector2D(0,settings.GAME_HEIGHT/2.)
        else :
            return Vector2D(settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)
    

    def placement_gardien_haut(self):
        return Vector2D(abs(self.position_mon_but().x-30),50)
    def placement_gardien_bas(self):
        return Vector2D(abs(self.position_mon_but().x-30),40)
    def placement_gardien_milieu(self):
        return Vector2D(abs(self.position_mon_but().x-30),45)
        
    def placement_campeur(self):
        return Vector2D(abs(self.position_mon_but().x-100),15)
    
    def placement_campeur_2(self):
        return Vector2D(abs(self.position_mon_but().x-100),75)
              
    def surface(self):
        if self.key[0]==1:
            return (self.ball_positionX()>settings.GAME_WIDTH-40)
        else :
            return (self.ball_positionX()<settings.GAME_WIDTH-110) 
    def position_dribble(self):
        return abs(self.position_mon_but().x-self.ball_positionX()) >= 65
    
    def placement_milieu_haut(self):
        return Vector2D(abs(self.position_mon_but().x-50),50)
    def placement_milieu_bas(self):
        return Vector2D(abs(self.position_mon_but().x-50),40)
    def placement_milieu_milieu(self):
        return Vector2D(abs(self.position_mon_but().x-50),45)
    
    def zone(self):
        L= self.state.get_zones(id_team)
        return L[0]


#==============================================================================#
#                               # Action                                       #
#==============================================================================#

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
        return self.aller(self.state.ball_position())
        
    def shoot(self, p):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1011)
            
    def shoot_passe(self, p):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1)
    
    def degagement(self):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(),self.state.position_but_adv()-self.state.my_position())
        else :
            return self.aller(self.state.ball_position())

        
    def mini_shoot(self, p):
        if self.state.zone_tir() :
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.0225)
        else :
            return self.aller(self.state.ball_position())
    
    
            
    def milieu_haut(self):
        if (self.state.distance_but_ball()>80):
            if self.state.ball_positionY()>50 and (self.state.distance_but_ball()<50):                    
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_milieu_haut())
        else:
            return self.passe()
    
    def milieu_bas(self):
        if (self.state.distance_but_ball()>80):
            if self.state.ball_positionY()>50 and (self.state.distance_but_ball()<50):                    
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_milieu_bas())
        else:
            return self.passe()
    
    def milieu_milieu(self):
        if (self.state.distance_but_ball()>80):
            if self.state.ball_positionY()>50 and (self.state.distance_but_ball()<50):                    
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_milieu_bas())
        else:
            return self.passe()
    
    def milieu(self):
        if self.state.ball_positionY()>50:
            return self.milieu_haut()
        elif self.state.ball_positionY()<40:
            return self.milieu_bas()
        else:
            return self.milieu_milieu()


            
    
    def gardien_haut(self):
        if (self.state.distance_but_ball()>70):
            if self.state.ball_positionY()>50 and (self.state.distance_but_ball()<65):                    
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_gardien_haut())
               
        else:
            return self.passe()    
            
    

    def gardien_bas(self):
        if (self.state.distance_but_ball()>70):
            if self.state.ball_positionY()<40 and (self.state.distance_but_ball()<65):                    
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_gardien_bas())
               
        else:
            return self.passe()   


    def gardien_milieu(self):
        if (self.state.distance_but_ball()>70):
            if self.state.ball_positionY()>40 and self.state.ball_positionY()<50 and (self.state.distance_but_ball()<65):                   
                return self.aller(self.state.ball_trajectoire_gardien())
            else :
                return self.aller(self.state.placement_gardien_milieu())
               
        else:
            return self.passe()                  

    def gardien(self):
        if self.state.ball_positionY()>50:
            return self.gardien_haut()
        elif self.state.ball_positionY()<40:
            return self.gardien_bas()
        else:
            return self.gardien_milieu()

                
    def dribbler(self):
        if (self.state.zone_tir()) and (self.state.distance_but_ball_att()<45):
            return self.shoot(self.state.position_but_adv())
        elif self.state.zone_tir():       
            return self.aller(self.state.ball_position())+ self.mini_shoot(self.state.position_but_adv()) 
        else:
            return self.aller(self.state.ball_position())
            
            
        
    def attaque_2vs2(self):
        if self.state.position_dribble():
            if not self.state.zone_tir():
                return self.aller(self.state.ball_position())
            elif not (self.state.surface()):
                return self.mini_shoot(self.state.position_but_adv())
            else :
                return self.shoot(self.state.position_but_adv())
        else :
            return self.aller(self.state.placement_campeur())
            

            
    def passe(self):
         if self.state.zone_tir():
             return self.shoot_passe(self.state.pos_joueur_plus_proche())
         else :
              return self.aller(self.state.ball_position())
             

    def attaque_2vs2_bis(self):
        if self.state.position_dribble():
            if not self.state.zone_tir():
                return self.aller(self.state.ball_position())
            elif not (self.state.surface()):
                return self.mini_shoot(self.state.position_but_adv())
            else :
                return self.shoot(self.state.position_but_adv())
        else :
            return self.aller(self.state.placement_campeur_2())
