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
	OF = ((OF[0]| OF[1] | OF[2] | Of[2])^1)
	less = SET[3]
	
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

