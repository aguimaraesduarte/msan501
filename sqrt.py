'''
sqrt(n)

x_0 = 1
x_{i+1} =0.5 * (x_i + n/x_i)
'''
import sys

def sqrt(n):
	PRECISION = 0.0000001
	x0 = 1.0
	xold = x0
	while True:
		print "x_i = %f" % xold
		xnew = 0.5 * (xold + n/xold)
		if abs(xnew - xold) < PRECISION: break
		xold = xnew
	return xnew

s = sqrt(int(sys.argv[1]))
print "sqrt(%d) is %f" % (int(sys.argv[1]), s)