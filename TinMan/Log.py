from sty import fg, bg, ef, rs

class Log:

    _instance = None

    def create():
        if log._instance == None:
            log._instance = log()
        
        return log._instance
    
    def __init__(self):
        return self
    
    def verbose(self,m):
        self.write_console(m, fg.gray, bg.black)

    def info(self,m):
        self.write_console(m, fg.white, bg.black)

    def warn(self,m):
        self.write_console(m, fg.magenta, bg.black)
    
    def error(self,m,ex):
        self.write_console(m + '\n' + str(ex), fg.white, bg.red)

    def write_console(self, m, foreground, background):
        print(foreground + background + m)

        

