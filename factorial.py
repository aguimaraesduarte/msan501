import sys

def factorial(n):
	if n < 0:
		print "%d is negative! Can't do that!" % n
		sys.exit(0)
	if n == 0: return 1
	return n*factorial(n-1)

print factorial(int(sys.argv[1]))

#number of bits required to store a number: log(n)