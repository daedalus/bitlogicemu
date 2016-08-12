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
        print "test 1"
        register = init_register(8)
        print register

        for i in range(0,16):
                register = LFSR(register,(1))
                print register

        print "test bit 0 ^ 1"
        register = init_register(8)
        print register

        for i in range(0,16):
                register = LFSR(register,(register[0] ^ 1))
                print register


def test_16bitfibbo_LFSR():
        print "test 16 bit fibbo "
        register = init_register(16)
        print register

        feedback = 1
        for i in range(0,16):
                register = LFSR(register,feedback)
                feedback = (register[10] ^ (register[12] ^ (register[13] ^ register[15])))
                print register,feedback

test_LFSR()
test_16bitfibbo_LFSR()
