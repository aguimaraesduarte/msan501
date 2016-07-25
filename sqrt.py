'''
sqrt(n)

x_0 = 1
x_{i+1} =0.5 * (x_i + n/x_i)
'''
import sys
import numpy as np

def sqrt(n):
	PRECISION = 0.000000001
	x0 = 1.0
	xold = x0
	while True:
		xnew = 0.5 * (xold + n/xold)
		if abs(xnew - xold) < PRECISION: break
		xold = xnew
	return xnew

def test_sqrt():
	def check(n):
		assert np.isclose(sqrt(n), np.sqrt(n))
	check(87291)
	check(100)
	check(0)
	check(1)
	check(2)


test_sqrt()