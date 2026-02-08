

	
def to_complex(value):
    """Convert a real number or tuple to a (real, imag) tuple."""
    if isinstance(value, tuple):
        return value
    else:
        return (float(value), 0.0)


def complex_add(first, second):
    a, b = to_complex(first)
    c, d = to_complex(second)
    return (a + c, b + d)


def complex_subtract(first, second):
    a, b = to_complex(first)
    c, d = to_complex(second)
    return (a - c, b - d)


def complex_multiply(first, second):
    a, b = to_complex(first)
    c, d = to_complex(second)
    return (a * c - b * d, a * d + b * c)


def complex_divide(first, second):
    a, b = to_complex(first)
    c, d = to_complex(second)
    denominator = c * c + d * d
    return ((a * c + b * d) / denominator, (b * c - a * d) / denominator)

	
#def real_to_complex(value):
#    """Convert a real number or list of real numbers to complex tuple(s)."""
#    if isinstance(value, (int, float)):
#        return (float(value), 0.0)
#    elif isinstance(value, (list, tuple)):
#        return [(float(v), 0.0) for v in value]
#    else:
#        raise TypeError("Input must be a real number or list/tuple of real numbers")


def real_to_complex(value):
    """Convert real numbers or complex tuples/lists into a consistent (re, im) tuple form."""
    if isinstance(value, (int, float)):
        return (float(value), 0.0)
    elif isinstance(value, tuple) and len(value) == 2:
        # Already a complex-like tuple
        return (float(value[0]), float(value[1]))
    elif isinstance(value, list):
        result = []
        for v in value:
            if isinstance(v, (int, float)):
                result.append((float(v), 0.0))
            elif isinstance(v, tuple) and len(v) == 2:
                result.append((float(v[0]), float(v[1])))
            else:
                raise TypeError(f"Invalid element in list: {v}")
        return result
    else:
        raise TypeError("Input must be a real number, tuple, or list of those")


def polynomial_coefficients(roots):
    """
    Compute polynomial coefficients for z^-1 form given roots.
    Roots can be complex or real.
    Returns coefficients:
        c[0] + c[1] z^-1 + ... + c[N] z^-N
    """
    coefficients = [(1.0, 0.0)]  # Start with 1
    for r in roots:
        # Convert real to complex if needed
        if isinstance(r, (int, float)):
            r = (float(r), 0.0)

        new_coefficients = [(0.0, 0.0)] * (len(coefficients) + 1)
        for i in range(len(coefficients)):
            new_coefficients[i] = complex_add(new_coefficients[i], coefficients[i])
            new_coefficients[i + 1] = complex_subtract(
                new_coefficients[i + 1],
                complex_multiply(r, coefficients[i])
            )
        coefficients = new_coefficients

    return coefficients

#def chebyshev(x, n):
#	'''
#	Chebyshev polynomial of order n
#	'''
#	if n > 1:
#		return 2 * x * chebyshev(x, n - 1) - chebyshev(x, n - 2)
#	elif n == 1:
#		return x
#	else: # n == 0
#		return 1

def chebyshev(x, n):
    """
    Chebyshev polynomial of order n.
    Supports both real and complex x (as tuples).
    """
    # Base cases
    if n == 0:
        return real_to_complex(1)
    elif n == 1:
        return real_to_complex(x)

    # Recursive relation: T_n(x) = 2x T_{n-1}(x) - T_{n-2}(x)
    t1 = chebyshev(x, n - 1)
    t2 = chebyshev(x, n - 2)

    # Handle multiplication by 2x
    two_x = complex_multiply(real_to_complex(2), real_to_complex(x))
    term = complex_multiply(two_x, t1)
    return complex_subtract(term, t2)

def bilinear_transform(value, is_s=True):
    """
    Perform bilinear transformation:
      if is_s:  z = (1 + s) / (1 - s)
      else:     s = (z - 1) / (z + 1)
    value can be a tuple (real, imag) or a real number.
    """
    v = to_complex(value)
    
    if is_s:
        numerator = complex_add(1, v)
        denominator = complex_subtract(1, v)
        z = complex_divide(numerator, denominator)
        return z
    else:
        numerator = complex_subtract(v, 1)
        denominator = complex_add(v, 1)
        s = complex_divide(numerator, denominator)
        return s
 
#TODO: Edit AI generated toy version of Parks-McClellan Algorithm
## START PARKS-MCCLELLAN

import numpy as np
import matplotlib.pyplot as plt

def remez_simple(numtaps, bands, desired, weight=None, grid_density=16, max_iter=25):
    """Simplified Remez exchange algorithm for linear-phase FIR (Type I)."""
    if weight is None:
        weight = [1.0] * len(desired)
    M = numtaps // 2  # Half order
    # Build dense frequency grid
    grid = np.linspace(0, np.pi, numtaps * grid_density)
    D = np.zeros_like(grid)
    W = np.zeros_like(grid)
    for i in range(0, len(bands), 2):
        idx = np.logical_and(grid >= bands[i] * np.pi, grid <= bands[i + 1] * np.pi)
        D[idx] = desired[i // 2]
        W[idx] = weight[i // 2]
    
    # Initialize extremal frequencies (M+2 points)
    extrema = np.linspace(0, np.pi, M + 2)
    delta = 1.0
    
    for iteration in range(max_iter):
        # Build linear system: A(ω_i) + (-1)^i δ/W_i = D(ω_i)
        A = np.cos(np.outer(extrema, np.arange(0, M + 1)))  # cosine matrix
        s = np.array([(-1)**i / W[np.argmin(np.abs(grid - w))] for i, w in enumerate(extrema)])
        rhs = D[np.searchsorted(grid, extrema)]
        # Append column for δ
        A = np.column_stack([A, s])
        coeffs = np.linalg.lstsq(A, rhs, rcond=None)[0]
        a = coeffs[:-1]
        delta = coeffs[-1]
        
        # Compute actual error on grid
        A_w = np.dot(np.cos(np.outer(grid, np.arange(0, M + 1))), a)
        E = W * (D - A_w)
        
        # Find new extremal frequencies (|E| peaks with sign alternation)
        sign_changes = np.where(np.diff(np.sign(E)))[0]
        candidates = np.concatenate(([0], sign_changes, [len(E)-1]))
        candidates = np.unique(candidates)
        peak_indices = np.argsort(np.abs(E[candidates]))[::-1][:M + 2]
        new_extrema = np.sort(grid[candidates[peak_indices]])
        
        # Check convergence
        if np.allclose(new_extrema, extrema, atol=1e-3):
            break
        extrema = new_extrema

    h = np.concatenate([a[::-1], a[1:]])  # symmetric impulse response
    return h, grid, D, E

##TODO: Fix below
if __name__ == "__main__":
    # Example: low-pass filter
    numtaps = 20
    bands = [0, 0.3, 0.4, 1.0]  # normalized frequencies (0–1 mapped to 0–π)
    desired = [1, 0]
    weights = [1, 10]

    h, w, D, E = remez_simple(numtaps, bands, desired, weights)

    # Plot result
    H = np.fft.fft(h, 4096)
    freqs = np.linspace(0, np.pi, len(H)//2)
    plt.figure(figsize=(8,4))
    plt.plot(freqs/np.pi, 20*np.log10(np.abs(H[:len(H)//2])))
    plt.title("Simplified Parks–McClellan FIR Design")
    plt.xlabel("Normalized Frequency (×π rad/sample)")
    plt.ylabel("Magnitude (dB)")
    plt.grid(True)
    plt.show()

    ## END PARKS-MCCLELLAN

