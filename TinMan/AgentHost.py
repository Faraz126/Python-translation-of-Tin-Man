import sys,math

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import RoboVizRemote,RoboVizExtensions,Shape,ShapeSet
from axel import Event
from datetime import timedelta

class AgentHost:
    default_tcp_port = 3100
    default_host_name = 'localhost'
    cycle_period_seconds = 0.02
    cycle_period = timedelta(cycle_period_seconds)
    _log = log.create()

    def __init__(self):
        self.host_name = AgentHost.default_host_name
        self.port_number = AgentHost.default_tcp_port
        self.team_name = 'TinManBots'
        _context = SimulationContext(self)
        self.context = _context
        self.has_run = None

    def _team_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('TeamName cannot be set after AgentHost.run has been called.'))
        if value == None:
            raise(BaseException('value'))
        self.team_name = value

    team_name = property(self.team_name, self._team_name_setter)

 
    def _host_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('HostName cannot be set after AgentHost.run has been called.'))
        if value == None:
            raise(BaseException('value'))
        if len(value.strip()) == 0:
            raise(BaseException('HostName cannot be blank ' + value))
        self.host_name = value

    host_name = property(self.host_name, self._host_name_setter)


    def _port_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('PortNumber cannot be set after AgentHost.run has been called.'))
        if value <= 0:
            raise(BaseException('value ' + str(value)+ ' PortNumber must be greater than zero' ))
        self.port_number = value

    port_name = property(self.port_name, self._port_name_setter)

    def run(self, agent):
        if agent == None:
            raise(BaseException('agent'))

        if self.has_run != None:
            raise(BaseException('Run can only be called once, and has already been called'))
        
        AgentHost._log.info('Connecting via TCP to' + self.host_name + ":" + str(self._port_name_setter))

        
