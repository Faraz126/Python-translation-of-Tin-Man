import sys
sys.path.append('../')

import angles, AngularSpeed, GeometryUtil,Polar,TransformationMatrix,Vector2,Vector3, io,math

class Token:
    kind = int()
    pos = int()
    col = int()
    line = int()
    val = str()
    
class Buffer:
    EOF = sys.maxsize + 1

class StringBuffer:

    def __init__(self, str):
        self.string = str
        self.pos =0

    def read(self):
        if self.pos = len(self.string):
            return Buffer.EOF
        self.pos += 1
        return self.string[self.pos-1]
    
    def peek(self):
        return self.string[self.pos]

class StreamBuffer:
    min_buffer_length = 1024
    max_buffer_length = StreamBuffer.min_buffer_length * 64
    '''
    buf = []
    buf_start = int()
    file_len = int()
    buf_pos = int()
    stream = io.StringIO()
    '''
    def __init__(self, s):
        self.stream = s
        if self.stream.seekable():
            self.file_len = len(self.stream)
            self.buf_len = math.min(self.file_len, StreamBuffer.max_buffer_length)
            self.buf_start = 2147483647
        else:
            self.file_len, self.buf_len,self.buf_start = 0,0,0
         
        if self.buf_len > 0:
            self.buf = list[None for i in self.buf_len]
        else:
            self.buf = list[None for i in StreamBuffer.min_buffer_length]
        
        if self.file_len > 0:
            self.pos = 0
        else:
            self.buf_pos = 0
        
    def read(self):
        if self.buf_pos < self.buf_len:
            self.buf_pos += 1
            return buf[self.buf_pos-1]
        elif self.pos < self.file_len:
            self.buf_pos  = self.pos
            self.buf_pos += 1
            return buf[self.buf_pos-1]
        elif not self.stream and not self.stream.seekable() and self.read_next_stream_chunk() > 0:
            self.buf_pos += 1
            return buf[self.buf_pos-1]
        else:
            return Buffer.EOF
        
    def peek(self):
        self.curpos = self.pos
        ch = self.read()
        self.pos = self.curpos
        return ch
    
    def _pos_getter(self):
        return self.buf_pos + self.buf_start
    
    def _pos_setter(self,value):
        if value >= self.file_len and not self.stream and not self.stream.seekable():
            while value >= file_len and self.read_next_stream_chunk() > 0:
        if value < 0 or value > self.file_len:
            raise BaseException('Buffer out of bounds access, position: ' + value)
        if value >= self.buf_start and value < self.buf_start + self.buf_len:
            self.buf_pos = value - self.buf_start
        elif not self.stream:
            self.stream.seek(value)
            self.buf_len = self.stream.read(buf,0,len(buf))
            self.buf_start = value
            self.buf_pos = 0
        else:
            self.buf_pos = self.file_len - self.buf_start
    
    def read_next_stream_chunk(self):
        free = len(buf) - self.buf_len
        if free == 0:
            new_buf = [None for i in self.buf_len*2]
        for i in range(len(self.buf)):
            new_buf[i] = buf[i]
        read = self.stream.Read(self.buf, self.buf_len, free)
        if read > 0:
            self.file_len, self.buf_len = self.buflen + read, self.buflen + read
            return read
        return 0

    class Scanner:
        EOL = '\n'
        eof_sym = 0
        max_t = 50
        no_sym = 50

        def __init__(self, *args):
            self.start = dict()
            for i in range(48,58):
                self.start[i] = 2
            for i in range(65,91):
                self.start[i] = 5
            for i in range(97,122):
                self.start[i] = 5
            self.start[45], self.start[40], self.start[41],self.start[Buffer.EOF] = 1,53,9,-1
            if args:
                if type(args[0] == str:
                    self.buffer = StringBuffer(s)
                    self.init()
                else:
                    self.buffer = StreamBuffer(s)
                    self.init()

        def init(self):
            self.pos = -1
            self.line = 1
            self.col = 0
            self.old_eols = 0
            self.nextch()

            self.pt = Token()
            self.tokens = Token()



    