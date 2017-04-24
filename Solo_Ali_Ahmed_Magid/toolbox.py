from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import settings
from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation
from soccersimulator.gui import SimuGUI,show_state,show_simu
import math

#==============================================================================#
#                               #Toolbox                                       #
#==============================================================================#



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
        return self.aller(self.state.ball_trajectoire())
        
    def shoot(self, p):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1011)
            
    def shoot_passe(self, p):
        if self.state.zone_tir():
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.1)
    
        
    def mini_shoot(self, p):
        if self.state.zone_tir() :
            return SoccerAction(Vector2D(), (p-self.state.my_position())*0.0225)
        else :
            return self.aller(self.state.ball_position())
    
    