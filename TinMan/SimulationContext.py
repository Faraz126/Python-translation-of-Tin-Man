from TinMan.Log import Log
from TinMan.PerceptorParsing.PerceptorState import FieldSide
from TinMan.PlayMode import PlayMode
from TinMan.Measures import Measures
from TinMan.EffectorCommands import Message, SayCommand,BeamCommand

class SimulationContext:
    _log = Log.create()

    def __init__(self, host):
        if host == None:
            raise(BaseException('host'))
        self._host = host
        self.team_side = FieldSide.unkwonn
        self.play_mode = PlayMode.unknown
        self.measures = Measures()
        self._beam_command = None
        self._say_command = None

    
    def say(self, msg_string):
        self._say_command = SayCommand(Message(msg_string))

    def beam(self, x,y,roation):
        if self.play_mode != PlayMode.before_kick_off or self.play_mode != PlayMode.goal_left or self.play_mode != PlayMode.goal_right:
           SimulationContext._log.warn('Requested beam during an invalid play mode: ' + str(self.play_mode))
        self._beam_command = BeamCommand(x,y,roation)

    def flush_commands(self, commands):
        if self._say_command != None:
            commands.append(self._say_command)
            self._say_command = None
        if self._beam_command != None:
            commands.append(self._beam_command)
            self._beam_command = None
    