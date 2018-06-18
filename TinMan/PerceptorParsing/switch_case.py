class SwitchCase:
    def __init__(self, num):
        self.state = num
    def check(self,**kwargs):
        num = self.state
        string = "SwitchCase.case_" + str(num).replace("-","_") + "(kwargs=kwargs)"
        out = eval(string)
        if out == None:
            t.val = str(self.tval)
            return t
    
    def case__1(**kwargs):
        t.kind = eof_sym
        
    
    def case_0(**kwargs):
        if self.rec_kind != no_sym:
            self.tlen = self.rec_end - t.pos
            self.set_scanner_behind()
        t.kind = self.rec_kind
        
    
    def case_1(**kwargs):
        if (self.ch >= '0' and self.ch <= "9"):
            self.add_ch()
            SwitchCase.case_2(kwargs = kwargs)
        else:
            SwitchCase.case_0(kwargs = kwargs)
    
    def case_2(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 1
        if (self.ch >= '0' and self.ch <= '9'):
            self.add_ch()
            SwitchCase.case_2(kwargs = kwargs)
        elif self.ch == '.':
            self.add_ch()
            SwitchCase.case_3(kwargs = kwargs)
        else:
            t.kind = 1
            
    
    def case_3(**kwargs):
        if self.ch >= '0' and self.ch <= '9':
            self.add_ch()    
            SwitchCase.case_4(kwargs = kwargs)
        else:
            SwitchCase.case_0(kwargs = kwargs)

    def case_4(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 1
        if self.ch >= '0' and self.ch <= '9':
            self.add_ch()
            SwitchCase.case_4(kwargs = kwargs)
        else:
            t.kind = 1
            
    def case_5(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 2
        if self.ch == '-' or (self.ch >= '0' and self.ch <= '9') or (self.ch >= 'A' and self.ch <= 'Z') or (self.ch >= 'a' and self.ch <= 'z'):
            self.add_ch()
            SwitchCase.case_5(kwargs = kwargs)
        else:
            t.kind = 2
            t.val = str(self.tval)
            self.check_literal()
            return t
        
    def case_6(**kwargs):
        if self.ch == 'o':
            self.add_ch()
            SwitchCase.case_7(kwargs = kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_7(**kwargs):
        if self.ch == 'l':
            self.add_ch()
            SwitchCase.case_8(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)

    def case_8(**kwargs):
        t.kind = 4
        
    
    def case_9(**kwargs):
        t.kind = 5
        
    
    def case_10(**kwargs):
        if self.ch == 'm':
            self.add_ch()
            SwitchCase.case_11(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_11(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_12(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_12(**kwargs):
        t.kind = 6
        
    
    def case_13(**kwargs):
        t.kind = 9
    
    def case_14(**kwargs):
        if self.ch == 'n':
            self.add_ch()
            SwitchCase.case_15(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_15(**kwargs):
        if self.ch == 'u':
            self.add_ch()
            SwitchCase.case_16(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_16(**kwargs):
        if self.ch == 'm':
            self.add_ch()
            SwitchCase.case_17(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_17(**kwargs):
        t.kind = 10
        
    
    def case_18(**kwargs):
        if self.ch == 'a':
            self.add_ch()
            SwitchCase.case_19(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_19(**kwargs):
        if self.ch == 'm':
            self.add_ch()
            SwitchCase.case_20(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_20(**kwargs):
        t.kind = 11
        
    
    def case_21(**kwargs):
        if self.ch == 'R':
            self.add_ch()
            SwitchCase.case_22(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_22(**kwargs):
        t.kind = 16
        
    
    def case_23(**kwargs):
        if self.ch == 'C':
            self.add_ch()
            SwitchCase.case_24(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_24(**kwargs):
        t.kind = 19
            
    def case_25(**kwargs):
        if self.ch == 'J':
            self.add_ch()
            SwitchCase.case_26(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_26(**kwargs):
        t.kind = 21
        

    def case_27(**kwargs):
        if self.ch == 'J':
            self.add_ch()
            SwitchCase.case_28(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_28(**kwargs):
        t.kind = 23
        
    
    def case_29(**kwargs):
        if self.ch == 'C':
            self.add_ch()
            SwitchCase.case_30(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_30(**kwargs):
        if self.ch == 'H':
            self.add_ch()
            SwitchCase.case_31(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_31(**kwargs):
        t.kind = 26
        
    
    def case_32(**kwargs):
        if self.ch == 'R':
            self.add_ch()
            SwitchCase.case_33(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_33(**kwargs):
        if self.ch == 'P':
            self.add_ch()
            SwitchCase.case_34(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_34(**kwargs):
        t.kind = 28
        
    
    def case_35(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_36(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_36(**kwargs):
        if self.ch == 'n':
            self.add_ch()
            SwitchCase.case_37(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)

    def case_37(**kwargs):
        if self.ch == 't':
            self.add_ch()
            SwitchCase.case_38(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_38(**kwargs):
        if self.ch == 'S':
            self.add_ch()
            SwitchCase.case_39(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_39(**kwargs):
        if self.ch == 't':
            self.add_ch()
            SwitchCase.case_40(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_40(**kwargs):
        if self.ch == 'a':
            self.add_ch()
            SwitchCase.case_41(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_41(**kwargs):
        if self.ch == 't':
            self.add_ch()
            SwitchCase.case_42(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_42(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_43(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_43(**kwargs):
        t.kind = 31
        
    
    def case_44(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_45(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_45(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_46(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_46(**kwargs):
        t.kind = 34
        
    
    def case_47(**kwargs):
        if self.ch == 'd':
            self.add_ch()
            SwitchCase.case_48(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_48(**kwargs):
        t.kind = 45
        
    
    def case_49(**kwargs):
        if self.ch == 'e':
            self.add_ch()
            SwitchCase.case_50(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_50(**kwargs):
        if self.ch =='a':
            self.add_ch()
            SwitchCase.case_51(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_51(**kwargs):
        if self.ch == 'r':
            self.add_ch()
            SwitchCase.case_52(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_52(**kwargs):
        t.kind = 48
        

    def case_53(**kwargs):
        self.rec_end = self.pos
        self.rec_kind = 7
        if self.ch == 'p':
            self.add_ch()
            SwitchCase.case_6(kwargs= kwargs)
        elif self.ch == 't':
            self.add_ch()
            SwitchCase.case_54(kwargs= kwargs)
        elif self.ch == 'G':
            self.add_ch()
            SwitchCase.case_55(kwargs= kwargs)
        elif self.ch == 'u':
            self.add_ch()
            SwitchCase.case_14(kwargs= kwargs)
        elif self.ch == 'A':
            self.add_ch()
            SwitchCase.case_56(kwargs= kwargs)
        elif self.ch == 'H':
            self.add_ch()
            SwitchCase.case_25(kwargs= kwargs)
        elif self.ch == 'U':
            self.add_ch()
            SwitchCase.case_27(kwargs= kwargs)
        elif self.ch == 'T':
            self.add_ch()
            SwitchCase.case_29(kwargs= kwargs)
        elif self.ch == 'F':
            self.add_ch()
            SwitchCase.case_32(kwargs= kwargs)
        elif self.ch == 'S':
            self.add_ch()
            SwitchCase.case_44(kwargs= kwargs)
        elif self.ch == 'i':
            self.add_ch()
            SwitchCase.case_47(kwargs= kwargs)
        elif self.ch == 'h':
            self.add_ch()
            SwitchCase.case_49(kwargs= kwargs)
        else:
            t.kind = 7
            
    
    def case_54(**kwargs):
        if self.ch == 'i':
            self.add_ch()
            SwitchCase.case_10(kwargs= kwargs)
        elif self.ch == 'e':
            self.add_ch()
            SwitchCase.case_18(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_55(**kwargs):
        if self.ch == 'S':
            self.add_ch()
            SwitchCase.case_13(kwargs= kwargs)
        elif self.ch == 'Y':
            self.add_ch()
            SwitchCase.case_21(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    def case_56(**kwargs):
        if self.ch == 'C':
            self.add_ch()
            SwitchCase.case_23(kwargs= kwargs)
        elif self.ch == 'g':
            self.add_ch()
            SwitchCase.case_35(kwargs= kwargs)
        else:
            SwitchCase.case_0(kwargs= kwargs)
    
    






            
    