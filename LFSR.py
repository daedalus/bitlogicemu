def init_register(n):
        return [0 for _ in range(0,n)]

def LFSR(register,FeedbackBit):
        new_register = init_register(len(register))
        for i in range(0,len(register)-1):
                new_register[i] = register[i+1]
        new_register[i+1] = FeedbackBit
        return new_register

def test_LFSR0():
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


def test_LFSR1():

	bits = 16
	steps = 16
	taps = [10,12,13,15]
	
        print "test 16 bit fibbo "
        print "https://en.wikipedia.org/wiki/Linear-feedback_shift_register"

 
        register = init_register(bits)
        print register

        feedback = 1
        feedback_bits = ""
        for i in range(0,steps):
                register = LFSR(register,feedback)
                feedback = (register[taps[0]] ^ (register[taps[1]] ^ (register[taps[2]] ^ register[taps[3]])))
                feedback_bits = feedback_bits + str(feedback)
                print register,feedback
        print feedback_bits,
        ifb = int(feedback_bits,2)
        print ifb,hex(ifb)


def bytetobits(char):
        return bin(ord(char))[2:]

def bitstobytes(bits):
        return sum(int(b) * (i**2) for i, b in enumerate(bits))

def CRC32(data):
	register = init_register(32)
	taps = [24,25,29,31]
	for i in range(len(data)):
		bits = bytetobits(data[i])
		for bit in bits:
			register = LFSR(register,bit)
			#print register,bit	
	
	return bitstobytes(register)

test_LFSR0()
test_LFSR1()

for i in range(0,16):
	message = 'hola man' + str(i)
	print message,hex(CRC32(message))

