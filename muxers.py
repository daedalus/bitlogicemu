#!/usr/bin/env python

def mux_1bit(a,b,X):
	return (a & (X ^ 1)) | (b & X) 

def mux_2bit(a,b,c,d,X0,X1):
	return (
		(a & (X1 ^ 1) & (X0 ^ 1))
		| (b & (X0 ^ 1) & X1)
		| (c & (X1 ^ 1) & X0)
		| (d & X0 & X1)
	)


