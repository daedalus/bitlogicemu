Q=0
Qp=0

def latchRS(R,S):
	global Q,Qp

	Q = (Qp ^ 1) | R
	Qp = (Q ^ 1) | S
 
	return Q,Qp
	
def latchD(C,D):
	R = (C & (D ^ 1))
	S = (C & D)
	Q,QP = flipflopRS(R,S)
	return Q,Qp
	
def flipflopDMasterSlave(D,C):
	Q,Qp = flipflopD(flipflopD(D,C),(C^1))
	return Q,Qp
	
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
