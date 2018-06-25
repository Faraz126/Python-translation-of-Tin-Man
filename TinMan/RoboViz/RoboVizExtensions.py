import sys

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import Shape

class RoboVizExtensions:
    def transform(transformation_matrix, line):
        return Shape.Line(transformation_matrix.transform(line.end1),transformation_matrix.transform(line.end2),line.pixel_thickness,line.color)
        