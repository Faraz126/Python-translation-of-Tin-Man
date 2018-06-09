class SwitchCase:
    def __init__(self, num):
        self.state = num
    def check(self,**kwargs):
        num = self.state
        string = "SwitchCase.case_" + str(num).replace("-","_") + "(kwargs=kwargs)"
        eval(string)
    
    def case__1(**kwargs):
        t.kind = eof_sym
        return
    
    def case_0((**kwargs):
        if self.rec_kind != no_sym:
            self.tlen = self.rec_end - t.pos
            self.set_scanner_behind()
        t.kind = self.rec_kind
        return
    
    def case_1(**kwargs):
        if (self.ch >= '0' and self.ch <= "9"):
            self.add_ch()
            case_2(kwargs = kwargs)
        else:
            case_0(kwargs = kwargs)
    
    def case_2(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 1
        if (self.ch >= '0' and self.ch <= '9'):
            self.add_ch()
            case_2(kwargs = kwargs)
        elif self.ch == '.':
            self.add_ch()
            case_3(kwargs = kwargs)
        else:
            t.kind = 1
            return
    
    def case_3(**kwargs):
        if self.ch >= '0' and self.ch <= '9':
            self.add_ch()    
            case_4(kwargs = kwargs)
        else:
            case_0(kwargs = kwargs)

    def case_4(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 1
        if self.ch >= '0' and self.ch <= '9':
            self.add_ch()
            case_4(kwargs = kwargs)
        else:
            t.kind = 1
            return