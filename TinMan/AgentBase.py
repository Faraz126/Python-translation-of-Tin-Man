import sys,math

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import RoboVizRemote,RoboVizExtensions,Shape,ShapeSet
from axel import Event


class AgentBase:
    def __init__(self, body):
        if body == None:
            raise(BaseException('body'))
        self.body = body
        self.log = log.create()
        self.is_alive = True
        self.think_completed = None
        self.shutting_down = None
        self._context = None
    
    measures = property(self._context.measures)

    Iagent_body = property(self.body)

    def __Iagent_context_getter__(self):
        if self._context == None:
            raise(BaseException('The context property cannot be accessed before the first call to think.'))
        return self._context
    def __Iagent_context_setter__(self,value):
        if value == None:
            raise(BaseException('value'))
        if self._context != None:
            raise(BaseException('Context has already been set.'))
        self._context = value

    Iagent_context = property(self.__Iagent_context_getter__, self.__Iagent_context_setter__)

    context = property(self.Iagent_context)

    def Iagent_think(self, state):
        self.think(state)
        evt = self.think_completed
        if evt != None:
            evt()
    
    def Iagent_on_shutting_down(self):
        self.on_shutdown()
        evt = self.shutting_down
        if evt != None:
            evt()
    
    def stop_simulation(self):
        self.log.info('Agent requested that the simulation stops')
        self.is_alive = False
        





