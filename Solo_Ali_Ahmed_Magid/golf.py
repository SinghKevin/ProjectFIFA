from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import toolbox
from strategy import *
GOLF = 0.001
SLALOM = 10.


class DemoStrategy(Strategy):
    def __init__(self):
        super(DemoStrategy,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return SoccerAction()
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        return SoccerAction()


class Slalom(Strategy):
    def __init__(self,name="Golfeur"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,id_team, id_player):
        m_pos = test_bis.Position(state,id_team,id_player)
        m_action = test_bis.Action(m_pos)
        zones=state.get_zones(id_team)
        if not m_pos.zone_tir():
            return m_action.aller_balle()
        elif len(zones)==0:
          print('-------------------------------------------------------------------------------------')
          return SoccerAction(Vector2D(),0.1011*(m_pos.position_but_adv()-m_pos.my_position()))
        else:
            zone=zones[0]
            if zone.dedans(state.ball.position):
                return m_action.aller_balle()
        return SoccerAction(Vector2D(),0.08*((zone.position+zone.l/2.)-m_pos.my_position()))

class Golfeur(Strategy):
    def __init__(self,name="Golfeur"):
        Strategy.__init__(self,name)
    def compute_strategy(self,state,id_team, id_player):
        m_pos = test_bis.Position(state,id_team,id_player)
        m_action = test_bis.Action(m_pos)
        zones=state.get_zones(id_team)
        if not m_pos.zone_tir():
            return m_action.aller_balle()
        elif len(zones)==0:
          print('-------------------------------------------------------------------------------------')
          return SoccerAction(Vector2D(),0.025*(m_pos.position_but_adv()-m_pos.my_position()))
        else:
            zone=zones[0]
            if zone.dedans(state.ball.position):
                return m_action.aller_balle()
        return SoccerAction(Vector2D(),0.025*((zone.position+zone.l/2.)-m_pos.my_position()))      
team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",Slalom())
team2.add("John",Slalom())
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team1,vitesse=SLALOM)
show_simu(simu)
simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
show_simu(simu)
