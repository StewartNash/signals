import math
import cmath

def twiddle_factor(n, k, N):
    return cmath.exp(-1j * 2 * math.pi * n * k / N)

def discrete_fourier_transform(x, k, N):
    output = 0 + 0j
    for n in range(N):
        output += x[n] * twiddle_factor(n, k, N)

    return output

def inverse_discrete_fourier_transform(X, n, N):
    output = 0 + 0j
    for k in range(N):
        output += X[k] * twiddle_factor(-n, k, N)
    
    return output

