Q=0
Qp=0

def flipflopRS(R,S):
	global Q,Qp

	Q = (Qp ^ 1) | R
	Qp = (Q ^ 1) | S
 
	return Q,Qp
	
def flipflopD(C,D)
	R = (C & (D ^ 1))
	S = (C & D)
	Q,QP = flipflopRS(R,S)
	return Q,Qp
	
def test_flipflopRS():

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


def test_flipflopD():

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

test_flipflopRS()
test_flipflopD()
