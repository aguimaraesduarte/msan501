import numpy as np

def minimize(f, x0, eta, h, precision):
	tracex = []
	xold = x0
	tracex.append(x0)
	while True:
		finite_diff = f(xold+h) - f(xold)
		xnew = xold - eta * finite_diff
		tracex.append(xnew)
		delta = f(xnew) - f(xold)
		if abs(delta) < precision and delta > 0: break
		xold = xnew
	return tracex

def f(x): return np.cos(3*np.pi*x) / x