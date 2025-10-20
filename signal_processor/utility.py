

	
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

	
def real_to_complex(value):
    """Convert a real number or list of real numbers to complex tuple(s)."""
    if isinstance(value, (int, float)):
        return (float(value), 0.0)
    elif isinstance(value, (list, tuple)):
        return [(float(v), 0.0) for v in value]
    else:
        raise TypeError("Input must be a real number or list/tuple of real numbers")

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

def bilinear_transformation(value, is_s=True):
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


