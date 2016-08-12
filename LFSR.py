#incomplete LFSR

def init_register(n):
        register = []
        for i in range(0,n):
                register.append(0)
        return register

def LFSR(register,FeedbackBit):
        new_register = init_register(len(register))
        for i in range(0,len(register)-1):
                new_register[i] = register[i+1]
        new_register[i+1] = FeedbackBit
        return new_register

def test_LFSR():
        register = init_register(8)
        print register

        for i in range(0,16):
                register = LFSR(register,(1)
                print register
        
        register = init_register(8)
        print register

        for i in range(0,16):
                register = LFSR(register,register[0] ^ 1))
                print register
      
        
def test_16bitfibbo_LFSR():
        register = init_register(8)
        print register
        
        feedback = 0
        for i in range(0,16):
                register = LFSR(register,feedback)
                feedback = (register[11] ^ (register[13] ^ (register[14] ^ register[16])))
                print register,feedback
      
test_LFSR()
test_16bitfibbo_LFSR()
