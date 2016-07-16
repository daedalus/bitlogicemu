#
# Author Dario Clavijo 2016
# GPLv3
#
# Inspired in the lectures of Allan Gottlieb 
# https://cs.nyu.edu/~gottlieb/courses/2000s/2007-08-fall/arch/lectures/lectures.html
#

def inv(i):
	return i ^ 1

def half_adder(a,b):
	s = a ^ b
	c = a & b
	return (c,s)

def full_adder(a,b,Cin):
	S =  ((a ^ b) ^ Cin)
	Cout = ((a & b) | ((a ^ b) & Cin))
	return (Cout,S)

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
	B,A = (a ^ i),(i ^ b)
	return (B,A)

def mux_1bit(a,b,X):
	Y = (a & (X ^ 1)) | (b & X)
	return (Y) 

def mux_2bit(a,b,c,d,X0,X1):
	Y = (a & (X1 ^ 1) & (X0 ^1)) | (b & (X0 ^1) & X1) | (c & (X1 ^1) & X0) | (d & X0 & X1)
	return Y


# this 1 bit ALU can support AND,OR,ADD,SLT,SUB,NOR Ops
# inputs a,b,aInvert,bInvert,less,CarryInput,Op0,Op1
# ouput CarryOut,Result,OverFlow,SET

def alu_1bit(a,b,aInv,bInv,less,Cin,Op0,Op1):	
	a,b = (a ^ aInv),(b ^ bInv)
	Cout,S = full_adder(a,b,Cin)
	Y = mux_2bit((a & b),(a | b),S,less,Op0,Op1)
	OF = (Cin ^ Cout)
	SET = (S ^ OF)
	return (Cout,Y,OF,SET)

#
# WIP
#
# this 4 bit ALU supports AND,OR,ADD,SLT,SUB,NOR Ops
# inputs a[0:4],b[0:4],aInvert,bNeg,Op0,Op1
# ouput CarryOut,Result[0:4],ZERO,OverFlow
#
# Func|Ctl_lns |aInv|bNeg| Ops
#-----|-----------------------------------------------
# AND |0 0 0 0 | 0  | 0  | 00
# OR  |0 0 0 1 | 0  | 0  | 01
# ADD |0 0 1 0 | 0  | 0  | 10
# SUB |0 1 1 0 | 0  | 1  | 10
# SLT |0 1 1 1 | 0  | 1  | 11
# NOR |1 1 0 0 | 1  | 1  | 00
#
# bNeg is a special case (bInv = Cin)
# ZERO = (A - B)

def alu_4bit(A,B,aInv,Bneg,Op0,Op1):

	less = 0  # retroalimentation: don't know how to put this, but I will assume that it starts = 0.
	Cout = [0,0,0,0]	
	Y = [0,0,0,0]
	OF = [0,0,0,0]
	SET = [0,0,0,0]

	Cout[0],Y[0],OF[0],SET[0] = alu_1bit(A[0],B[0],aInv,bNeg,less,bNeg,Op0,Op1)
	Cout[1],Y[1],OF[1],SET[1] = alu_1bit(A[1],B[1],aInv,bNeg,0,Cout[0],Op0,Op1)
	Cout[2],Y[2],OF[2],SET[2] = alu_1bit(A[2],B[2],aInv,bNeg,0,Cout[1],Op0,Op1)
	Cout[3],Y[3],OF[3],SET[3] = alu_1bit(A[3],B[3],aInv,bNeg,0,Cout[2],Op0,Op1)
	
	ZERO = ((Y[0]| Y[1] | Y[2] | Y[2])^1)
	OF = ((OF[0]| OF[1] | OF[2] | Of[2])^1)
	less = SET[3]
	Cout = Cout[3]	
	return (Cout,Y,ZERO,OF)

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

def test_mux1_bit():
	print "mux_1bit"
	print "a,b,X -> Y"
	print "0,0,0",mux_1bit(0,0,0)
	print "0,0,1",mux_1bit(0,0,1)
	print "0,1,0",mux_1bit(0,1,0)
	print "0,1,1",mux_1bit(0,1,1)
	print "1,0,0",mux_1bit(1,0,0)
	print "1,0,1",mux_1bit(1,0,1)
	print "1,1,0",mux_1bit(1,1,0)
	print "1,1,1",mux_1bit(1,1,1)
	print

def test_mux_2bit():
	print "mux_2bit"
	print "a,b,c,d,X0,X1 -> Y"
	print mux_2bit(0,0,0,0,0,0)
	print mux_2bit(0,0,0,0,1,0)
	print mux_2bit(0,0,0,0,1,1)
	print mux_2bit(0,0,0,1,0,0)
	print mux_2bit(0,0,0,1,0,1)
	print mux_2bit(0,0,0,1,1,0)
	print mux_2bit(0,0,0,1,1,1)
	print mux_2bit(0,0,1,0,0,0)
	print mux_2bit(0,0,1,0,0,1)
	print mux_2bit(0,0,1,0,1,0)
	print mux_2bit(0,0,1,0,1,1)
	print mux_2bit(0,0,1,1,0,0)
	print mux_2bit(0,0,1,1,0,1)
	print mux_2bit(0,0,1,1,1,0)
	print mux_2bit(0,0,1,1,1,1)
	print mux_2bit(0,1,0,0,0,0)
	print mux_2bit(0,1,0,0,0,1)
	print mux_2bit(0,1,0,0,1,0)
	print mux_2bit(0,1,0,0,1,1)
	print mux_2bit(0,1,0,1,0,0)
	print mux_2bit(0,1,0,1,0,1)
	print mux_2bit(0,1,0,1,1,0)
	print mux_2bit(0,1,0,1,1,1)
	print mux_2bit(0,1,1,0,0,0)
	print mux_2bit(0,1,1,0,0,1)
	print mux_2bit(0,1,1,0,1,0)
	print mux_2bit(0,1,0,0,1,1)
	print mux_2bit(0,1,0,1,0,0)
	print mux_2bit(0,1,0,1,0,1)
	print mux_2bit(0,1,0,1,1,0)
	print mux_2bit(0,1,0,1,1,1)
	print mux_2bit(0,1,1,0,0,0)
	print mux_2bit(0,1,1,0,0,1)
	print mux_2bit(0,1,1,0,1,0)
	print mux_2bit(0,1,1,0,1,1)
	print mux_2bit(0,1,1,1,0,0)
	print mux_2bit(0,1,1,1,0,1)
	print mux_2bit(0,1,1,1,1,0)
	print mux_2bit(0,1,1,1,1,1)
	print mux_2bit(1,0,0,0,0,0)
	print mux_2bit(1,0,0,0,1,0)
	print mux_2bit(1,0,0,0,1,1)
	print mux_2bit(1,0,0,1,0,0)
	print mux_2bit(1,0,0,1,0,1)
	print mux_2bit(1,0,0,1,1,0)
	print mux_2bit(1,0,0,1,1,1)
	print mux_2bit(1,0,1,0,0,0)
	print mux_2bit(1,0,1,0,0,1)
	print mux_2bit(1,0,1,0,1,0)
	print mux_2bit(1,0,1,0,1,1)
	print mux_2bit(1,0,1,1,0,0)
	print mux_2bit(1,0,1,1,0,1)
	print mux_2bit(1,0,1,1,1,0)
	print mux_2bit(1,0,1,1,1,1)
	print mux_2bit(1,1,0,0,0,0)
	print mux_2bit(1,1,0,0,0,1)
	print mux_2bit(1,1,0,0,1,0)
	print mux_2bit(1,1,0,0,1,1)
	print mux_2bit(1,1,0,1,0,0)
	print mux_2bit(1,1,0,1,0,1)
	print mux_2bit(1,1,0,1,1,0)
	print mux_2bit(1,1,0,1,1,1)
	print mux_2bit(1,1,1,0,0,0)
	print mux_2bit(1,1,1,0,0,1)
	print mux_2bit(1,1,1,0,1,0)
	print mux_2bit(1,1,0,0,1,1)
	print mux_2bit(1,1,0,1,0,0)
	print mux_2bit(1,1,0,1,0,1)
	print mux_2bit(1,1,0,1,1,0)
	print mux_2bit(1,1,0,1,1,1)
	print mux_2bit(1,1,1,0,0,0)
	print mux_2bit(1,1,1,0,0,1)
	print mux_2bit(1,1,1,0,1,0)
	print mux_2bit(1,1,1,0,1,1)
	print mux_2bit(1,1,1,1,0,0)
	print mux_2bit(1,1,1,1,0,1)
	print mux_2bit(1,1,1,1,1,0)
	print mux_2bit(1,1,1,1,1,1)
	print

def test_alu1bit():
	print "FIXME"
	print 

def test_truth_tables():
	test_inv()
	test_half_adder()
	test_Full_Adder()
	test_four_bit_adder()
	test_eight_bit_adder()
	test_bitswap()
	test_test_mux1_bit()
	
test_truth_tables()
