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
        print "https://en.wikipedia.org/wiki/Linear-feedback_shift_register"
        bits = 16
        steps = 16
 
        register = init_register(bits)
        print register

        feedback = 1
        feedback_bits = ""
        for i in range(0,steps):
                register = LFSR(register,feedback)
                feedback = (register[10] ^ (register[12] ^ (register[13] ^ register[15])))
                feedback_bits = feedback_bits + str(feedback)
                print register,feedback
        print feedback_bits,
        ifb = int(feedback_bits,2)
        print ifb,hex(ifb)


test_LFSR()
test_16bitfibbo_LFSR()
