import angles, AngularSpeed, GeometryUtil

class Polar: #Immutable Data type
    def __init__(self,distance,theta,phi):
        '''
        Theta = Angle in horizontal plane, 0 means point towards opponent goal
        Phi = Lattidunial angle. 0 = Horizontal, -ve = point downward '''
        if distance < 0:
            raise BaseException("Distance", distance, "must not be negative")
        self.distance = distance
        self.theta = theta
        self.phi = phi

    def to_vector3(self):
        t = Distance * self.phi.cos
        x = t * self.theta.cos
        y = t * self.theta.sin
        z = Distance*self.phi.sin

        return vector3(x,y,z) #need addition

    def is_zero(self):
        return self.distance == 0 and self.theta == Angle(0) and self.phi == Angle(0)

    def to_string(self):
        return "Distance: " + str(round(self.distance,2)) + ", Theta: " + str(round(self.theta,2)) + ", Phi: " +str(round(self.degrees,2)) 
    
