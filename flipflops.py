Q=0
Qneg=0

# inputs: R,S R=reset,S=Set
# outputs: Q, QNeg (Q is always = NOT Qneg)
def latchRS(R,S):
	global Q,Qneg
	
	Q = (R | Qp) ^ 1
        Qp = (S | Q) ^ 1
 
	return Q,Qneg

# inputs: C,D C=Clock, D=Data
# outputs: Q,Qneg (Q is always = NOT Qneg)
def latchD(C,D):
	global Q,Qneg
        
	R = (C & (D ^ 1))
	S = (C & D)
	
	Q,Qneg = flipflopRS(R,S)
	return Q,Qneg

# inputs: C,D C=Clock, D=Data
# outputs: Q,Qneg (Q is always = NOT Qneg)
def flipflopDMasterSlave(D,C):
	Q,Qneg = latchD((C^1),latchD(C,D))
	return Q,Qneg
	
def test_latchRS():
	# keep the internal state 10 clocks
	for i in range(10):
        	print "0,0",flipflopRS(0,0)
	
	# simulate a set
	print "0,1",flipflopRS(0,1)
	
	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopRS(0,0)

	# simulate a reset
	print "1,0",flipflopRS(1,0)

	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopRS(0,0)

	# simulate a invalid state
	for i in range(10):
        	print "1,1",flipflopRS(1,1)

def test_latchD():
	# keep the internal state 10 clocks
	for i in range(10):
        	print "0,0",flipflopD(0,0)
	
	# simulate a set
	print "0,1",flipflopD(0,1)
	
	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopD(0,0)

	# simulate a reset
	print "1,0",flipflopD(1,0)

	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopD(0,0)

	# simulate a invalid state
	for i in range(10):
        	print "1,1",flipflopD(1,1)
        	
def test_flipflopDMasterSlave():
	# keep the internal state 10 clocks
	for i in range(10):
        	print "0,0",flipflopDMasterSlave(0,0)
	
	# simulate a set
	print "0,1",flipflopDMasterSlave(0,1)
	
	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopDMasterSlave(0,0)

	# simulate a reset
	print "1,0",flipflopDMasterSlave(1,0)

	# keep the internal state 10 clocks
	for i in range(10):
		print "0,0",flipflopDMasterSlave(0,0)

	# simulate a invalid state
	for i in range(10):
        	print "1,1",flipflopDMasterSlave(1,1)

def tests():
	test_latchRS()
	test_latchD()
	test_flipflopDMasterSlave()
