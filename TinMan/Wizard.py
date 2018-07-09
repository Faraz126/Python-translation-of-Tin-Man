from Log import Log
import socket
from NetworkUtil import NetworkUtil
from SExpressionReader import SExpressionReader
from datetime import timedelta
from Geometry.TransformationMatrix import TransformationMatrix
from PerceptorParsing.PerceptorState import FieldSide
from Geometry.Vector3 import Vector3

class Wizard:
    default_tcp_port = 3200
    default_host_name = 'localhost'
    _log = Log.create()

    def __init__(self):
        self.host_name = Wizard.default_host_name
        self.port_number = Wizard.default_tcp_port
        self.ball_transform_updated= None
        self.agent_transform_updated = None

    def run(self):
        Wizard._log.info("Connecting via TCP to " + self.host_name + ":" str(self.port_number))

        try:
            client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            client.connect((self.host_name, self.port_number))
        except:
            AgentHost._log.Error('Unable to connect to '+ self.host_name+ " : "+ self.port_number)
            raise(BaseException())
        
        Wizard._log.info('Connected.')
        self._is_running = True


        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
            client.connect((self.host_name, self.port_number))
            while self._is_running:
                length = NetworkUtil.get_length(client, 5)

                if length == 0:
                    Wizard._log('Ignoring zero-length message recieved from server.')
                    continue
                
                sexp = SExpressionReader(client, length)

                ball_event = self.ball_transform_updated
                agent_event = self.agent_transform_updated

                if ball_event != None or agent_event != None:
                    game_time = timedelta()
                    
                    if sexp.in(2):
                        if sexp.take() == 'time':
                            time_val = sexp.take()
                            secs = float(time_val)
                            game_time = timedelta(time_val)
                    
                    sexp.out(2)

                    if sexp.skip(1) and sexp.in(1) and sexp.skip(35) and sexp.in(1) and sexp.skip(1) and sexp.in(1) and sexp.skip(1):
                        transform = Wizard.try_read_transform_matrix(sexp)

                        if transform[0] and ball_event != None:
                            ball_event(game_time, transform[1])

                        if agent_event != None and sexp.out(2):
                            done = False

                            while not done:

                                if sexp.in(3):
                                    transform = Wizard.try_read_transform_matrix(sexp)
                                    if sexp.take() == 'SLT' and transform[0]:
                                        agent_event(game_time, transform[1])
                                    if not sexp.out(3):
                                        done = True
                                else:
                                    done = True
            sexp.skip_to_end()


    def try_read_transform_matrix(sexp):

        values = [float() for i in range(8)]
        for i in range(16):
            s = sexp.take()

            if s == None:
                return False, None 

            try:
                d = float(s)

            except ValueError:
                  return False, None
            
            values[i] = d

        transform = TransformationMatrix(values)
        return True, transform
    
    def stop(self):
        self._is_running = False

    def get_side_string(team_side):
        if team_side == FieldSide.left:
            return 'Left'
        elif team_side == FieldSide:
            return 'Right'
        elif team_side == FieldSide:
            return 'None'
        else:
            raise(BaseException('Unexpected valued for fieldside num' + str(team_side)))

    def get_vector_string(vector):
        return str(vector.x)+ " " + str(vector.y) + " " + str(vector.z)




