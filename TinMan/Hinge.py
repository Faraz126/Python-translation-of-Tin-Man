import sys,math

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import RoboVizRemote,RoboVizExtensions,Shape,ShapeSet

from datetime import timedelta
import AgentHost

class Hinge:
    def __init__(self, perceptor_label, effector_label, min_angle, max_angle):
        if perceptor_label == None:
            raise(BaseException('Perceptor_Label'))
        if effector_label == None:
            raise(BaseException('Effector_label'))
        if max_angle < min_angle:
            raise(BaseException('max_angle cannot be less than min_angle'))
        self.perceptor_label = perceptor_label
        self.effector_label = effector_label
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.angle = None
        self.is_desired_speed_changed = None
        self._desired_speed = AngularSpeed.AngularSpeed(math.nan)
        self._control_function = False


    def _speed_setter(self, value):
        self._control_function = None
        self.set_desired_speed_internal(value)

    desired_speed = property(self._desired_speed, self._speed_setter)


    def get_commmand(self):
        if not is_desired_speed_changed:
            raise(BaseException('The speed value for this hinge was not changed. Check is_speed_changed before calling this method'))
        self.is_desired_speed_changed = False
        return HingeSpeedCommand(self, self.desired_speed)

    def set_desired_speed_internal(self, desired_speed):
        if self._desired_speed == desired_speed:
            return
        self._desired_speed = desired_speed
        self.is_desired_speed_changed = True

    def set_control_function(self,control_function):
        self._control_function = control_function
    
    def clear_control_function(self):
        self._control_function = None
    
    def has_control_function(self):
        return self._control_function != None

    def compute_control_funcition(self, context, perceptor_state):
        fun = self._control_function
        if fun == None:
            return

        desired_speed = fun(this,context, perceptor_state)

        if not math.isnan(desired_speed):
            self.set_desired_speed_internal(desired_speed)

    def validate_angle(self, angle):
        if angle.isnan:
            raise(BaseException('angle Nan is invalid as an angle'))
        if not self.is_angle_valid(angle):
            raise(BaseException('angle ' + str(angle) + " is not a valid angle for hinge "+ self.effector_label+'. The range is between ' + str(self.min_angle)+ ' and ' + str(self.max_angle) + '.' ))

    def is_angle_valid(self, angle):
        return self.max_angle >= angle >= self.min_angle

    def limit_angle(self,angle):
        return angle.limit(self.min_angle, self.max_angle)
        
        