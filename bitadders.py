#!/usr/bin/env python

# inputs: a,b
# outputs: c,s C=Carry, S=Sum(A,B)
def half_adder(a,b):
	S = a ^ b
	C = a & b
	return (C,S)

# inputs: a,b,Cin Cin=CarryIn
# outputs: Cout,S Cout=CarryOut,S=Sum(A,B)
def full_adder(a,b,Cin):
	S =  ((a ^ b) ^ Cin)
	Cout = ((a & b) | ((a ^ b) & Cin))
	return (Cout,S)

# inputs: A[0:4], B[0:4]
# outputs C,S[0:4] Cout=CarryOut, S=Sum(A,B)
def four_bit_adder(A,B,Cin):
	S = [0,0,0,0]
	C,s = full_adder(A[0],B[0],Cin)
	S[0] = s
	C,s = full_adder(A[1],B[1],C)
	S[1] = s
	C,s = full_adder(A[2],B[2],C)
	S[2] = s
	C,s = full_adder(A[3],B[3],C)
	S[3] = s
	Cout = C
	return (Cout,S)

# inputs: A[0:4], B[0:4]
# outputs C,S[0:4] Cout=CarryOut, S=Sum(A,B)
def eight_bit_adder(A,B,Cin):
	S = [0,0,0,0,0,0,0,0]
	C,s = four_bit_adder(A[:4], B[:4], Cin)
	S += s
	C,s = four_bit_adder(A[4:8],B[4:8],C)
	S += s
	Cout = C
	return (Cout,S)



#
# tests zone
#

def test_inv():
	print "Inv"
	print "i -> o"
	print "0",inv(0)
	print "1",inv(1)
	print

def test_half_adder()
	print "half Adder"
	print "a,b -> C,S"
	print "0,0",half_adder(0,0)
	print "0,1",half_adder(0,1)
	print "1,0",half_adder(1,0)
	print "1,1",half_adder(1,1)
	print 

def test_Full_Adder():
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

def test_four_bit_adder():
	print "four bit adder"
	print "a + b -> c,s"
	print four_bit_adder([1,1,1,1],[1,0,0,0],0)
	print	

def test_eight_bit_adder():
	print "eight bit adder"
	print "a + b -> c,s"
	print eight_bit_adder([1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0],0)
	print

def test_bitswap():
	print "bitswap"
	print "a,b -> B,A"
	print "0,0",swap2bits(0,0)
	print "0,1",swap2bits(0,1)
	print "1,0",swap2bits(1,0)
	print "1,1",swap2bits(1,1)
	print

def test_truth_tables():
	test_half_adder()
	test_Full_Adder()
	test_four_bit_adder()
	test_eight_bit_adder()

	
test_truth_tables()
