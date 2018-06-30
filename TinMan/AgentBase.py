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
