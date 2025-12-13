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

# AI code to modify

def fft_dit(x):
    """
    Radix-2 Decimation-In-Time FFT
    x: list of complex samples, length must be power of 2
    """
    N = len(x)

    if N == 1:
        return x

    if N & (N - 1) != 0:
        raise ValueError("Length of input must be a power of 2")

    # Split even and odd indices
    X_even = fft_dit(x[0::2])
    X_odd  = fft_dit(x[1::2])

    # Combine
    X = [0] * N
    for k in range(N // 2):
        twiddle = cmath.exp(-2j * math.pi * k / N)
        t = twiddle * X_odd[k]

        X[k] = X_even[k] + t
        X[k + N // 2] = X_even[k] - t

    return X
    
def bit_reverse_indices(N):
    bits = int(math.log2(N))
    indices = []

    for i in range(N):
        b = format(i, f'0{bits}b')
        indices.append(int(b[::-1], 2))

    return indices


def fft_dit_iterative(x):
    """
    In-place radix-2 DIT FFT (iterative)
    """
    N = len(x)
    if N & (N - 1) != 0:
        raise ValueError("Length must be power of 2")

    # Bit-reversal permutation
    indices = bit_reverse_indices(N)
    X = [x[i] for i in indices]

    # FFT stages
    stage = 1
    while stage <= int(math.log2(N)):
        m = 2 ** stage
        half = m // 2
        Wm = cmath.exp(-2j * math.pi / m)

        for k in range(0, N, m):
            W = 1
            for j in range(half):
                t = W * X[k + j + half]
                u = X[k + j]
                X[k + j] = u + t
                X[k + j + half] = u - t
                W *= Wm

        stage += 1

    return X
    
    def ifft_dit(X):
    """
    Inverse FFT using radix-2 DIT FFT
    """
    N = len(X)

    # Conjugate input
    X_conj = [x.conjugate() for x in X]

    # Forward FFT
    x = fft_dit(X_conj)

    # Conjugate again and scale
    return [val.conjugate() / N for val in x]
    
    def ifft_dit_iterative(X):
    """
    Inverse FFT (iterative radix-2 DIT)
    """
    N = len(X)

    # Conjugate
    X_conj = [x.conjugate() for x in X]

    # Forward FFT
    x = fft_dit_iterative(X_conj)

    # Conjugate and normalize
    return [val.conjugate() / N for val in x]
    
