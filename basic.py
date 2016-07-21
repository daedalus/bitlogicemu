#!/usr/bin/env python

# input i
# output = NOT i
def inv(i):
	return i ^ 1

# inputs a,b
# outputs a,b -> b,a
def swap2bits(a,b):
	i = (a ^ b)
	B,A = (a ^ i),(i ^ b)
	return (B,A)

def test_truth_tables():
	test_inv()
	test_bitswap()
