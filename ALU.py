#!/usr/bin/env python
#
# Author Dario Clavijo 2016
# GPLv3
#
# Inspired in the lectures of Allan Gottlieb 
# https://cs.nyu.edu/~gottlieb/courses/2000s/2007-08-fall/arch/lectures/lectures.html
#  
# The intention of this POC is to provide the internals of a microprocesor architecrure 
# pure implemented in boole logic, avoiding python internal control structures like
# if,while,for,etc and atomic data types. 
# But there is a catch, how we can implement feedback without recursion.
#
import bitadders
import muxers


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

less = 0  # retroalimentation: don't know how to put this, but I will assume that it starts = 0.
def alu_4bit(A,B,aInv,Bneg,Op0,Op1):

	global less
	Cout = [0,0,0,0]	
	Y = [0,0,0,0]
	OF = [0,0,0,0]
	SET = [0,0,0,0]

	Cout[0],Y[0],OF[0],SET[0] = alu_1bit(A[0],B[0],aInv,bNeg,less,bNeg,Op0,Op1)
	Cout[1],Y[1],OF[1],SET[1] = alu_1bit(A[1],B[1],aInv,bNeg,0,Cout[0],Op0,Op1)
	Cout[2],Y[2],OF[2],SET[2] = alu_1bit(A[2],B[2],aInv,bNeg,0,Cout[1],Op0,Op1)
	Cout[3],Y[3],OF[3],SET[3] = alu_1bit(A[3],B[3],aInv,bNeg,0,Cout[2],Op0,Op1)
	
	ZERO = ((Y[0]| Y[1] | Y[2] | Y[2])^1)
	OF = (OF[0]| OF[1] | OF[2] | Of[2])
	less = SET[3]
	
	return (Cout,Y,ZERO,OF)

#
# WIP
#
# this 8 bit ALU supports AND,OR,ADD,SLT,SUB,NOR Ops
# inputs a[0:8],b[0:8],aInvert,bNeg,Op0,Op1
# ouput CarryOut,Result[0:8],ZERO,OverFlow
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

less = 0  # retroalimentation: don't know how to put this, but I will assume that it starts = 0.
def alu_8bit(A,B,aInv,Bneg,Op0,Op1):

	global less
	Cout = [0,0,0,0,0,0,0,0]	
	Y = [0,0,0,0,0,0,0,0]
	OF = [0,0,0,0,0,0,0,0]
	SET = [0,0,0,0,0,0,0,0]

	Cout[0],Y[0],OF[0],SET[0] = alu_1bit(A[0],B[0],aInv,bNeg,less,bNeg,Op0,Op1)
	Cout[1],Y[1],OF[1],SET[1] = alu_1bit(A[1],B[1],aInv,bNeg,0,Cout[0],Op0,Op1)
	Cout[2],Y[2],OF[2],SET[2] = alu_1bit(A[2],B[2],aInv,bNeg,0,Cout[1],Op0,Op1)
	Cout[3],Y[3],OF[3],SET[3] = alu_1bit(A[3],B[3],aInv,bNeg,0,Cout[2],Op0,Op1)
	Cout[4],Y[4],OF[4],SET[4] = alu_1bit(A[4],B[4],aInv,bNeg,0,Cout[3],Op0,Op1)
	Cout[5],Y[5],OF[5],SET[5] = alu_1bit(A[5],B[5],aInv,bNeg,0,Cout[4],Op0,Op1)
	Cout[6],Y[6],OF[6],SET[6] = alu_1bit(A[6],B[6],aInv,bNeg,0,Cout[5],Op0,Op1)
	Cout[7],Y[7],OF[7],SET[7] = alu_1bit(A[7],B[7],aInv,bNeg,0,Cout[6],Op0,Op1)
	
	ZERO = ((Y[0]| Y[1] | Y[2] | Y[3] | Y[4] | Y[5] | Y[6] | Y[7]) ^ 1)
	OF = (OF[0]| OF[1] | OF[2] | OF[3] | OF[4] | OF[5] | OF[6] | OF[7]) 
	less = SET[7]
	
	return (Cout,Y,ZERO,OF)

#
# WIP
#
# this 16 bit ALU supports AND,OR,ADD,SLT,SUB,NOR Ops
# inputs a[0:16],b[0:16],aInvert,bNeg,Op0,Op1
# ouput CarryOut,Result[0:16],ZERO,OverFlow
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

less = 0  # retroalimentation: don't know how to put this, but I will assume that it starts = 0.
def alu_16bit(A,B,aInv,Bneg,Op0,Op1):

	global less
	Cout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	
	Y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	OF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	SET = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	Cout[0],Y[0],OF[0],SET[0] = alu_1bit(A[0],B[0],aInv,bNeg,less,bNeg,Op0,Op1)
	Cout[1],Y[1],OF[1],SET[1] = alu_1bit(A[1],B[1],aInv,bNeg,0,Cout[0],Op0,Op1)
	Cout[2],Y[2],OF[2],SET[2] = alu_1bit(A[2],B[2],aInv,bNeg,0,Cout[1],Op0,Op1)
	Cout[3],Y[3],OF[3],SET[3] = alu_1bit(A[3],B[3],aInv,bNeg,0,Cout[2],Op0,Op1)
	Cout[4],Y[4],OF[4],SET[4] = alu_1bit(A[4],B[4],aInv,bNeg,0,Cout[3],Op0,Op1)
	Cout[5],Y[5],OF[5],SET[5] = alu_1bit(A[5],B[5],aInv,bNeg,0,Cout[4],Op0,Op1)
	Cout[6],Y[6],OF[6],SET[6] = alu_1bit(A[6],B[6],aInv,bNeg,0,Cout[5],Op0,Op1)
	Cout[7],Y[7],OF[7],SET[7] = alu_1bit(A[7],B[7],aInv,bNeg,0,Cout[6],Op0,Op1)
	Cout[8],Y[8],OF[8],SET[8] = alu_1bit(A[8],B[8],aInv,bNeg,0,Cout[7],Op0,Op1)
	Cout[9],Y[9],OF[9],SET[9] = alu_1bit(A[9],B[9],aInv,bNeg,0,Cout[8],Op0,Op1)
	Cout[10],Y[10],OF[10],SET[10] = alu_1bit(A[10],B[10],aInv,bNeg,0,Cout[9],Op0,Op1)
	Cout[11],Y[11],OF[11],SET[11] = alu_1bit(A[11],B[11],aInv,bNeg,0,Cout[10],Op0,Op1)
	Cout[12],Y[12],OF[12],SET[12] = alu_1bit(A[12],B[12],aInv,bNeg,0,Cout[11],Op0,Op1)
	Cout[13],Y[13],OF[13],SET[13] = alu_1bit(A[13],B[13],aInv,bNeg,0,Cout[12],Op0,Op1)
	Cout[14],Y[14],OF[14],SET[14] = alu_1bit(A[14],B[14],aInv,bNeg,0,Cout[13],Op0,Op1)
	Cout[15],Y[15],OF[15],SET[15] = alu_1bit(A[15],B[15],aInv,bNeg,0,Cout[14],Op0,Op1)
	
	ZERO = ((Y[0]| Y[1] | Y[2] | Y[3] | Y[4] | Y[5] | Y[6] | Y[7] 
			| Y[8] | Y[9] | Y[10] | Y[11] | Y[12] | Y[13] | Y[14] | Y[15]) ^ 1)
			
	OF = (OF[0]| OF[1] | OF[2] | OF[3] | OF[4] | OF[5] | OF[6] | OF[7]
			| OF[8] | OF[9] | OF[10] | OF[11] | OF[12] | OF[13] | OF[14] | OF[15]) 
	less = SET[15]
	
	return (Cout,Y,ZERO,OF)

#
# WIP
#
# this 32 bit ALU supports AND,OR,ADD,SLT,SUB,NOR Ops
# inputs a[0:32],b[0:32],aInvert,bNeg,Op0,Op1
# ouput CarryOut,Result[0:32],ZERO,OverFlow
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

less = 0  # retroalimentation: don't know how to put this, but I will assume that it starts = 0.
def alu_32bit(A,B,aInv,Bneg,Op0,Op1):

	global less
	Cout = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]	
	Y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	OF = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	SET = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	Cout[0],Y[0],OF[0],SET[0] = alu_1bit(A[0],B[0],aInv,bNeg,less,bNeg,Op0,Op1)
	Cout[1],Y[1],OF[1],SET[1] = alu_1bit(A[1],B[1],aInv,bNeg,0,Cout[0],Op0,Op1)
	Cout[2],Y[2],OF[2],SET[2] = alu_1bit(A[2],B[2],aInv,bNeg,0,Cout[1],Op0,Op1)
	Cout[3],Y[3],OF[3],SET[3] = alu_1bit(A[3],B[3],aInv,bNeg,0,Cout[2],Op0,Op1)
	Cout[4],Y[4],OF[4],SET[4] = alu_1bit(A[4],B[4],aInv,bNeg,0,Cout[3],Op0,Op1)
	Cout[5],Y[5],OF[5],SET[5] = alu_1bit(A[5],B[5],aInv,bNeg,0,Cout[4],Op0,Op1)
	Cout[6],Y[6],OF[6],SET[6] = alu_1bit(A[6],B[6],aInv,bNeg,0,Cout[5],Op0,Op1)
	Cout[7],Y[7],OF[7],SET[7] = alu_1bit(A[7],B[7],aInv,bNeg,0,Cout[6],Op0,Op1)
	
	Cout[8],Y[8],OF[8],SET[8] = alu_1bit(A[8],B[8],aInv,bNeg,0,Cout[7],Op0,Op1)
	Cout[9],Y[9],OF[9],SET[9] = alu_1bit(A[9],B[9],aInv,bNeg,0,Cout[8],Op0,Op1)
	Cout[10],Y[10],OF[10],SET[10] = alu_1bit(A[10],B[10],aInv,bNeg,0,Cout[9],Op0,Op1)
	Cout[11],Y[11],OF[11],SET[11] = alu_1bit(A[11],B[11],aInv,bNeg,0,Cout[10],Op0,Op1)
	Cout[12],Y[12],OF[12],SET[12] = alu_1bit(A[12],B[12],aInv,bNeg,0,Cout[11],Op0,Op1)
	Cout[13],Y[13],OF[13],SET[13] = alu_1bit(A[13],B[13],aInv,bNeg,0,Cout[12],Op0,Op1)
	Cout[14],Y[14],OF[14],SET[14] = alu_1bit(A[14],B[14],aInv,bNeg,0,Cout[13],Op0,Op1)
	Cout[15],Y[15],OF[15],SET[15] = alu_1bit(A[15],B[15],aInv,bNeg,0,Cout[14],Op0,Op1)

	Cout[16],Y[16],OF[16],SET[16] = alu_1bit(A[16],B[16],aInv,bNeg,0,Cout[15],Op0,Op1)
	Cout[17],Y[17],OF[17],SET[17] = alu_1bit(A[17],B[17],aInv,bNeg,0,Cout[16],Op0,Op1)
	Cout[18],Y[18],OF[18],SET[18] = alu_1bit(A[18],B[18],aInv,bNeg,0,Cout[17],Op0,Op1)
	Cout[19],Y[19],OF[19],SET[19] = alu_1bit(A[19],B[19],aInv,bNeg,0,Cout[18],Op0,Op1)
	Cout[20],Y[20],OF[20],SET[20] = alu_1bit(A[20],B[20],aInv,bNeg,0,Cout[19],Op0,Op1)
	Cout[21],Y[21],OF[21],SET[21] = alu_1bit(A[21],B[21],aInv,bNeg,0,Cout[20],Op0,Op1)
	Cout[22],Y[22],OF[22],SET[22] = alu_1bit(A[22],B[22],aInv,bNeg,0,Cout[21],Op0,Op1)
	Cout[23],Y[23],OF[23],SET[23] = alu_1bit(A[23],B[23],aInv,bNeg,0,Cout[22],Op0,Op1)	
	
	Cout[24],Y[24],OF[24],SET[24] = alu_1bit(A[24],B[24],aInv,bNeg,0,Cout[23],Op0,Op1)
	Cout[25],Y[25],OF[25],SET[25] = alu_1bit(A[25],B[25],aInv,bNeg,0,Cout[24],Op0,Op1)
	Cout[26],Y[26],OF[26],SET[26] = alu_1bit(A[26],B[26],aInv,bNeg,0,Cout[25],Op0,Op1)
	Cout[27],Y[27],OF[27],SET[27] = alu_1bit(A[27],B[27],aInv,bNeg,0,Cout[26],Op0,Op1)
	Cout[28],Y[28],OF[28],SET[28] = alu_1bit(A[28],B[28],aInv,bNeg,0,Cout[27],Op0,Op1)
	Cout[29],Y[29],OF[29],SET[29] = alu_1bit(A[29],B[29],aInv,bNeg,0,Cout[28],Op0,Op1)
	Cout[30],Y[30],OF[30],SET[30] = alu_1bit(A[30],B[30],aInv,bNeg,0,Cout[29],Op0,Op1)
	Cout[31],Y[31],OF[31],SET[31] = alu_1bit(A[31],B[31],aInv,bNeg,0,Cout[30],Op0,Op1)	
	
	
	ZERO = ((Y[0]| Y[1] | Y[2] | Y[3] | Y[4] | Y[5] | Y[6] | Y[7] 
			| Y[8] | Y[9] | Y[10] | Y[11] | Y[12] | Y[13] | Y[14] | Y[15]) 
			| Y[16] | Y[17] | Y[18] | Y[19] | Y[20] | Y[21] | Y[22] | Y[23] 
			| Y[24] | Y[25] | Y[26] | Y[27] | Y[28] | Y[29] | Y[30] | Y[31] ^ 1)
			
	OF = (OF[0]| OF[1] | OF[2] | OF[3] | OF[4] | OF[5] | OF[6] | OF[7]
			| OF[8] | OF[9] | OF[10] | OF[11] | OF[12] | OF[13] | OF[14] | OF[15]
			| OF[16] | OF[17] | OF[18] | OF[19] | OF[20] | OF[21] | OF[22] | OF[23] 
			| OF[24] | OF[25] | OF[26] | OF[27] | OF[28] | OF[29] | OF[30] | OF[31]) 
	less = SET[31]
	
	return (Cout,Y,ZERO,OF)


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

