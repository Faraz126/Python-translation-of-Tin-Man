import sys,math

from Geometry import angles,AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3
from PerceptorParsing import switch_case,Parser,Scanner,PerceptorState
from RoboViz import RoboVizRemote,RoboVizExtensions,ShapeSet

class Shape:
    def __init__(self):
        self._is_visible = True
        self.shape_set = None
    
    def is_visible_setter(self,value):
        if value == self.is_visible:
            return
        else:
            self._is_visible = value
            self.set_dirty()

    is_visible = property(self._is_visible, self.is_visible_setter)

    def remove(self):
        if self.shape_set == None:
            raise(BaseException('This shape cannot be removed as it is not currently contained within a shapeset.'))
        self.shape_set.remove()

    def set_shape_set(self, shape_set): 
        if shape_set == None:
            raise(BaseException('shape_set'))
        if self.shape_set == None:
            raise(BaseException('Shape already belongs to Shapeset' + str(self.shape_set.path) + ' so cannot be added to ' + str(shape_set.path)))
        self.shape_set = shape_set

    def clear_set_shape_set(self):
        if self.shape_set == None:
            raise(BaseException('Shape doesnt belong to a shapeSet'))
        self.shape_set = None

    def set_dirty(self):
        if self.shape_set != None:
            self.shape_set.is_dirty = True

    def write_double(buf, offset, d):
        assert not math.isnan(d) , 'Float value may not be Nan'
        s = str(round(d,6))
        s = [0:min(len(s),6)]
        assert len(s) == 6, 'Formatting of float value ' + str(d) + ' should be 6 characters long but was ' + str(len(s))
        bytes_temp = bytes(s[0:6], 'ascii')
        bytes_count = len(bytes_temp)
        for i in range(len(bytes_temp)):
            buf[offset+i] = bytes_temp[i]
        assert bytes_count == 6, 'Should have 6 bytes but instead have' + str(bytes_count)
    
    def write_color(buf,offset,color, include_alpha):
        buf[offset+1] = color.R
        buf[offset+2] = color.G
        buf[offset+3] = color.B
        if include_alpha:
            buf[offset+4] = color.A
    
    def validate_double(value):
        if math.isnan(value):
            raise(BaseException('Value' + str(value) + 'Cannot be NaN')
        if math.isinf(value):
            raise(BaseException('value' + str(value) + 'cannot be infinite'))

class Dot(Shape):

    def __init__(self, pixel_size = 5, color = color.white, position = Vector3.Vector3()):
        self._pixel_size = pixel_size
        self._color = color
        self.position = position
        self._x = self.position.x
        self._y = self.position.y
        self._z = self.position.z
        super().__init__()

    def _pixel_size_setter_(self,value):
        super(Dot,Dot).validate_double(value)
        self._pixel_size = value
        self.set_dirty()

    pixel_size = property(self._pixel_size, self._pixel_size_setter_)

    def _color_setter_(self,value):
        self._color = value
        self.set_dirty()

    color = property(self._color, self._color_setter_)

    def _position_setter(self, value):
        self._x = value.x
        self._y = value.y
        self._z = value.z
    
    position = property(Vector3(self.x,self.y,self.z),self._position_setter)

    def _x_setter(self,value):
        super(Dot,Dot).validate_double(value)
        self._x = value
        self.set_dirty()

    def _y_setter(self,value):
        super(Dot,Dot).validate_double(value)
        self._y = value
        self.set_dirty()

    def _z_setter(self,value):
        super(Dot,Dot).validate_double(value)
        self._z = value
        self.set_dirty()

    x = property(self._x, self._x_setter)
    y = property(self._y, self._y_setter)
    z = property(self._z, self._z_setter)

    def translate(self,offset):
        self.position += offset
    
    def send_message(self, udp_client):
        path_bytes = self.shape_set.path_bytes
        num_bytes = 30 + len(path_bytes)
        buf = [None for i in range(num_bytes)]
        buf[0] = 1
        buf[1] = 2
        super(Dot,Dot).write_double(buf,2, self._x)
        super(Dot,Dot).write_double(buf,8, self._y)
        super(Dot,Dot).write_double(buf,14, self._z)
        super(Dot,Dot).write_double(buf,20, self.pixel_size)
        super(Dot,Dot).write_color(buf,26,color, False)
        for i in range(len(path_bytes)):
            buf[29+i] = path_bytes[i]
        bytes_sent_count = udp_client.send(buf, len(buf))
        assert bytes_sent_count == num_bytes


class Line(Shape):

    def __init__(self, end1 = Vector3.Vector3(), end2 = Vector3.Vector3(), pixel_thickness = 1, color = color.white):
        self._pixel_thickness = pixel_thickness 
        self._color = color
        self.end1 = end1
        self._x1 = end1.x
        self._y1 = end1.y
        self._z1 = end1.z 
        self.end2 = end2
        self._x2 = end2.x
        self._y2 = end2.y
        self._z3 = end2.z
        super().__init()

    def _end1_setter(self,value):
        self.x1 =  value.x
        self.y1 = value.y
        self.z1 = value.z

    end1 = property(Vector3.Vector3(self._x,self._y,self._z), self._end1_setter)

    def _end2_setter(self,value):
        self.x2 =  value.x
        self.y2 = value.y
        self.z2 = value.z

    end2 = property(Vector3.Vector3(self._x,self._y,self._z), self._end2_setter)

    def _x1_setter(self,value):
        super(Line,Line).validate_double(value)
        self._x1 = value
        self.set_dirty()

    x1 = property(self._x1, self._x1_setter)

    def _y1_setter(self,value):
        super(Line,Line).validate_double(value)
        self._y1 = value
        self.set_dirty()

    y1 = property(self._y1, self._y1_setter)

    def _z1_setter(self,value):
        super(Line,Line).validate_double(value)
        self._z1 = value
        self.set_dirty()

    z1 = property(self._z1, self._z1_setter)

    def _x2_setter(self,value):
        super(Line,Line).validate_double(value)
        self._x2 = value
        self.set_dirty()

    x2 = property(self._x2, self._x2_setter)

    def _y2_setter(self,value):
        super(Line,Line).validate_double(value)
        self._y2 = value
        self.set_dirty()

    y2 = property(self._y2, self._y2_setter)

    def _z2_setter(self,value):
        super(Line,Line).validate_double(value)
        self._z2 = value
        self.set_dirty()

    z2 = property(self._z2, self._z2_setter)

    def _pixel_thickness_setter(self, value):
        super(Line,Line).validate_double(value)
        self._pixel_thickness = value
        self.set_dirty()

    pixel_thickness = property(self._pixel_thickness, self._pixel_thickness_setter)

    def _color_setter(self, value):
        self._color = color
        self.set_dirty()

    color = property(self._color, self._color_setter)

    def translate(self,offset):
        self.end1 += offset
        self.end2 += offset

    def send_message(self, udp_client):
        path_bytes = self.shape_set.path_bytes
        num_bytes = 48 + len(path_bytes)
        buf = [i for i in range(num_bytes)]

        buf[0] = 1
        buf[1] = 1
        super(Line,Line).write_double(buf,2, self._x1)
        super(Line,Line).write_double(buf,8, self._y1)
        super(Line,Line).write_double(buf,14, self._z1)
        super(Line,Line).write_double(buf,20, self._x2)
        super(Line,Line).write_double(buf,26, self._y2)
        super(Line,Line).write_double(buf,32, self._z2)
        super(Line,Line).write_double(buf,38, self.pixel_thickness)
        super(Line,Line).write_color(buf, 44, color, False)
        for i in range(len(path_bytes)):
            buf[47+i] = path_bytes[i]
        bytes_sent_count = udp_client.sent(buf, len(buf))
        assert bytes_sent_count == num_bytes

        
