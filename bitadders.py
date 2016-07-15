#
# Author Dario Clavijo 2016
# GPLv3
#

def inv(i):
	return i ^ 1

def half_adder(a,b):
	s = a ^ b
	c = a & b
	return (c,s)

def full_adder(a,b,Cin):
	s =  ((a ^ b) ^ Cin)
	Cout = ((a & b) | ((a ^ b) & Cin))
	return (Cout,s)

def four_bit_adder(A,B,Cin):
	Sum = [0,0,0,0]
	c,s = full_adder(A[0],B[0],Cin)
	Sum[0] = s
	c,s = full_adder(A[1],B[1],c)
	Sum[1] = s
	c,s = full_adder(A[2],B[2],c)
	Sum[2] = s
	c,s = full_adder(A[3],B[3],c)
	Sum[3] = s

	Cout = c
	return (Cout,Sum)

def eight_bit_adder(A,B,Cin):
	S = [0,0,0,0,0,0,0,0]
	c,s = four_bit_adder(A[0:4],B[0:4],Cin)
	S += s	
	c,s = four_bit_adder(A[4:8],B[4:8],c)
	S += s
	
	Cout = c
	return (Cout,S)


def swap2bits(a,b):
	i = (a ^ b)
	B,A = (a ^ i),(b ^ i)
	return (A,B)

def test_truth_tables():
	print "Inv"
	print "i -> o"
	print "0",inv(0)
	print "1",inv(1)
	print

	print "half Adder"
	print "a,b -> C,S"
	print "0,0",half_adder(0,0)
	print "0,1",half_adder(0,1)
	print "1,0",half_adder(1,0)
	print "1,1",half_adder(1,1)
	print 

	print "Full Adder"
	print "a,b,Cin -> C,S"
	print "0,0,0",full_adder(0,0,0)
	print "0,0,1",full_adder(0,0,1)
	print "0,1,0",full_adder(0,1,0)
	print "0,1,1",full_adder(0,1,1)
	print "1,0,0",full_adder(1,0,0)
	print "1,0,1",full_adder(1,0,1)
	print "1,1,0",full_adder(1,1,0)
	print "1,1,1",full_adder(1,1,1)
	print 	

	print "four bit adder"
	print "a + b -> c,s"
	print four_bit_adder([1,1,1,1],[1,0,0,0],0)
	
	print "eight bit adder"
	print "a + b -> c,s"
	print eight_bit_adder([1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0],0)


test_truth_tables()
