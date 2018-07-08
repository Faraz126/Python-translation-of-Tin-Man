import sockets
import struct
from Log import Log
import time

class NetworkUtil:
    _log = Log.create()

    def write_string_with_32_bit_length_prefex(client, msg):

        payload = msg.encode('ascii')
        prefix = struct.pack('!I', len(payload))
        client.send(prefix + payload)

    def read_response_string(client, timeout):
        c_time = time.time()
        while time.time() - c_time < timeout:
            prefix = client.recv(4)
            if prefix != b"":
                break
            elif time.time() - c_time >= timeout:
                NetworkUtil._log.warn('No response recieved within time limit')
                return None
            
        if not prefix:
            NetworkUtil._log.warn('No response recieved within time limit')
            return None

        payload_length = struct.unpack('!I', prefix)
        raw_payload = client.recv(payload_length[0])
        payload = raw_payload.decode('ascii')
        return payload







