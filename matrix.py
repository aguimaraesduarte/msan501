def identity(N):
	'''Return NxN identity matrix'''
	I = [] # make an empty list
	for i in range(N): # i in [0..N)
		row = [0] * N  # make row of N zeroes
		row[i] = 1	 # set the ith column to 1
		I.append(row)  # add a row to end of list
	return I

print identity(5)

def mprint(A):
	N = len(A)
	for i in range(N):
		for j in range(N):
			print A[i][j],
		print

print
mprint(identity(5))

def identity2(N):
	I = [[0] * N for i in range(N)]  # make N x N matrix
	for i in range(N): # set the diagonal to 1
		I[i][i] = 1    # set the ith row, ith column to 1
	return I

print
mprint(identity2(5))

def zero(N, initial=0):
	return [[initial] * N for i in range(N)]  # make N x N matrix

def identity3(N):
	I = zero(N)
	for i in range(N):
		I[i][i] = 1    # set the ith row, ith column to 1
	return I

print
mprint(identity3(5))

def set_diagonal(A, x):
	N = len(A)
	for i in range(N):
		A[i][i] = x  # set the ith row, ith column to 1

def identity4(N):
	I = zero(N)  # make N x N matrix
	set_diagonal(I, 1)
	return I

print
mprint(identity4(5))

def diagonal(N, x):
	A = zero(N)  # make N x N matrix
	set_diagonal(A, x)
	return A

def identity5(N):
	return diagonal(N, 1)

print
mprint(identity5(5))

print
mprint(diagonal(5, "a"))


def scale(A,x):
	"Scale matrix A by x in place; don't create a new one"
	N = len(A)
	for i in range(N):
		for j in range(N):
			A[i][j] *= x
	return A

print
A = identity(4)
scale(A,5)
mprint(A)

def apply(A,f):
	#"Apply function f to every element of matrix A in place"
	N = len(A)
	for i in range(N):
		for j in range(N):
			A[i][j] = f(A[i][j]) # replace A[i][j]
	return A

print
A = identity(4)
def mult(x) : return 5 * x # this is applied to each element
apply(A, mult)
mprint(A)

print
A = identity(4)
apply(A, lambda x : 5 * x) # lambdas are just anonymous functions
mprint(A)

print
apply(A, lambda x : 3.0 * x) # mult by floating-point
mprint(A)
