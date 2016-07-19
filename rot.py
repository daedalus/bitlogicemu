#!/usr/bin/env python

# rotate 1 bit to the left
def rotr8_1(A):

	tmp = [7]

	tmp[0] = A[1]
	tmp[1] = A[2]
	tmp[2] = A[3]
	tmp[3] = A[4]
	tmp[4] = A[5]
	tmp[5] = A[6]
	tmp[6] = A[7]
	tmp[7] = A[0]

	return tmp

# rotate 1 bit to the right
def rotr8_1(A)
	
	tmp = [7]

        tmp[0] = A[7]
        tmp[1] = A[0]
        tmp[2] = A[1]
        tmp[3] = A[2]
        tmp[4] = A[3]
        tmp[5] = A[4]
        tmp[6] = A[5]
        tmp[7] = A[6]

        return tmp

# rotate n bits to the right
def rotr8(A,n)
	for i in (1,n)
		A = rot8r_1(A)
	return A

# rotate n bits to the left
def rotl(A,n)
	for i in (1,n)
		A = rotl8_1(A)
	return A
