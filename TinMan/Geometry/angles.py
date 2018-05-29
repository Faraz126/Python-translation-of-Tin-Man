import math
import random

class Angle:
    epsilon = 0.0001
    '''
    zero = Angle(0)
    two_pi = Angle(math.pi*2)
    half_pi = Angle(math.pi/2)
    pi = Angle(math.pi)
    nan = Angle(math.nan)
    '''
    
    #Region Factory Methods
    
    def random():
        return Angle((random.randint(0,200)/100)*math.pi)

    def from_radians(radians):
        return Angle(radians)

    def from_degree(degrees):
        return Angle(Angle.degrees_to_radians(degrees))

    def a_cos(d):
        return Angle.from_radians(math.acos(d))

    def a_tan(d):
        return Angle.from_radians(math.atan(d))

    def a_tan2(x,y):
        return Angle.from_radians(math.atan2(x,y))

    def __init__(self,radians):
        self.radians = radians
        

    #end region



    #Region Utility Methods

    def degrees_to_radians(degrees):
        factor = math.pi/180
        return degrees*factor

    def radians_to_degrees(radians):
        factor = 180/math.pi
        return radians*factor

    #end region

    #Properties #Need to use decorator here

    def degrees(self):
        return Angle.radians_to_degrees(self.radians)

    def cos(self):
        return math.cos(self.radians)

    def sin(self):
        return math.sin(self.radians)

    def tan(self):
        return math.sin(self.radians)

    def is_nan(self):
        return math.isnan(self.radians)

    def abs(self):
        return Angle(abs(self.radians))

    #end properties

    def normalise_balanced(self):
        new = self.radians

        while new < math.pi:
            new += math.pi*2
        while new >= math.pi:
            new -= math.pi*2
        return Angle.from_radians(new)

    #region operators, equality, hashing

    def equals(self,obj):
        return type(obj) == type(self) and self.equals_2(obj)

    def equals_2(self,other):
        return (self.is_nan() and other.is_nan()) or abs(other.radians-self.radians) < self.epsilon

    def get_hash_code(self):
        return hash(self.radians)

    def __add__(a,b):
        return Angle.from_radians((a.radians + b.radians))

    def __mul__(a,b):
        return Angle.from_radians((a.radians * b.radians))

    def __sub__(a,b):
        return Angle.from_radians((a.radians - b.radians))


    def __truediv__(a,b):
        if type(b) != Angle:
            return from_radians(a.radians/b) #Code to be added after time class
        return Angle.from_radians(a.radians/b.radians)

    def __gt__(a,b):
        return a.radians > b.radians

    def __lt__(a,b):
        return a.radians < b.radians

    def __ge__(a,b):
        return a.radians >= b.radians

    def __le__(a,b):
        return a.radians <= b.radians

    def __eq__(a,b):
        return a.equals(b)

    def __ne__(a,b):
        return not a.equals(b)

    #to_string method left




    
    
