import sys,math

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import RoboVizRemote,RoboVizExtensions,Shape,ShapeSet
from axel import Event
from datetime import timedelta
import socket

class AgentHost:
    default_tcp_port = 3100
    default_host_name = 'localhost'
    cycle_period_seconds = 0.02
    cycle_period = timedelta(cycle_period_seconds)
    _log = log.create()

    def __init__(self):
        self._host_name = AgentHost.default_host_name
        self._port_number = AgentHost.default_tcp_port
        self._team_name = 'TinManBots'
        _context = SimulationContext(self)
        self.context = _context
        self.has_run = None
        self._stop_requested = False

    def _team_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('TeamName cannot be set after AgentHost.run has been called.'))
        if value == None:
            raise(BaseException('value'))
        self._team_name = value

    team_name = property(self._team_name, self._team_name_setter)

    def _desired_uniform_number_setter(self, value):
        if self.has_run != None:
            raise(BaseException('Desired_Uniform_number cannot be set after AgentHost.run has been called.'))
        if value < 0:
            raise(BaseException('Value '+ str(value)+ ' The desired uniform number must be zero or a positive integer'))
        self._desired_uniform_number = value

    desired_uniform_number = property(self._desired_uniform_number, self._desired_uniform_number_setter)


    def _host_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('HostName cannot be set after AgentHost.run has been called.'))
        if value == None:
            raise(BaseException('value'))
        if len(value.strip()) == 0:
            raise(BaseException('HostName cannot be blank ' + value))
        self._host_name = value

    host_name = property(self._host_name, self._host_name_setter)


    def _port_name_setter(self,value):
        if self.has_run != None:
            raise(BaseException('PortNumber cannot be set after AgentHost.run has been called.'))
        if value <= 0:
            raise(BaseException('value ' + str(value)+ ' PortNumber must be greater than zero' ))
        self._port_number = value

    port_name = property(self._port_name, self._port_name_setter)

    def run(self, agent):
        if agent == None:
            raise(BaseException('agent'))

        if self.has_run != None:
            raise(BaseException('Run can only be called once, and has already been called'))
        
        AgentHost._log.info('Connecting via TCP to' + self.host_name + ":" + str(self._port_name_setter))

        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect((self.host_name, self.port_number))
        except:
            AgentHost._log.Error('Unable to connect to '+ self.host_name+ " : "+ self.port_number)
            raise(BaseException())
        
        AgentHost._log.info('Connected.')
        self.has_run = True
        AgentHost._log.info('Initializing agent')
        agent.context = self.context
        agent.on_initialise()

        with client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
            client.connect((self.host_name, self.port_number))
            self._log('Sending initialisation messages')
            send_commands(client, SceneSpecificationCommand(agent.body.rsg_path)
            NetworkUtil.read_response_string(client, 0.5)

            send_commands(client, InitialisePlayerCommand(self.desired_uniform_number, self.team_name))
            NetworkUtil.read_response_string(client, 0.5)

            commands = list()

            while not self._self_requested and agent.is_alive:
                data = NetworkUtil.read_response_string(client, 0.1)

                if not data:
                    continue

                parser = Parser.Parser(Scanner.Scanner(Scanner.StringBuffer(data)))
                parser.parse()
                perceptor_state = parser.state
                errors = parser.errorrs
            
            if errors.has_error:
                AgentHost._log.error('Parse Error: ' errors.error_messages + '\nData:' + data)

            for hinge in agent.body.all_hinges:
                angle = perceptor_state.try_get_hinge_angle(hinge)
                if angle != False:
                    hinge.angle = angle

                if perceptor_state.team_side !=  PerceptorState.FieldSide.unkwonn:
                    self.context.team_side = perceptor_state.team_side

                if perceptor_state.play_mode != PlayMode.PlayMode.unkwonn and perceptor_state.play_mode != self.context.play_mode:
                    self.context.play_mode = perceptor_state.play_mode

                if perceptor_state.uniform_number.has_value:
                    assert perceptor_state.uniform_number > 0:
                    self.context.uniform_number = perceptor_state.uniform_number

                agent.Think(perceptor_state)

                for hing in agent.body.all_hinges:
                    hinge.compute_control_function(self.context, perceptor_state)
                
                self._context.flush_commands(commands)



    
