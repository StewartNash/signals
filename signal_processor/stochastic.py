import numpy as np

def wiener_coefficients(x, s, M):
    """
    Compute Wiener filter coefficients
    
    x : noisy input signal
    s : desired signal
    M : filter length
    """
    N = len(x)
    
    # Build data matrix
    X = np.zeros((N - M + 1, M))
    for i in range(M):
        X[:, i] = x[M - 1 - i : N - i]

    s_vec = s[M - 1:]

    # Autocorrelation matrix
    T = (X.T @ X) / len(s_vec)

    # Cross-correlation vector
    v = (X.T @ s_vec) / len(s_vec)

    # Wiener solution
    h = np.linalg.solve(T, v)
    
    return h


def complex_wiener_coefficients(x, d, M):
    """
    Compute complex Wiener filter coefficients
    
    x : complex noisy input signal
    d : complex desired signal
    M : filter length
    """
    x = np.asarray(x, dtype=np.complex128)
    d = np.asarray(d, dtype=np.complex128)

    N = len(x)
    if len(d) != N:
        raise ValueError("x and d must have same length")

    # Build data matrix
    X = np.zeros((N - M + 1, M), dtype=np.complex128)
    for i in range(M):
        X[:, i] = x[M - 1 - i : N - i]

    d_vec = d[M - 1:]

    # Autocorrelation matrix Rxx = E[x x^H]
    Rxx = (X.conj().T @ X) / len(d_vec)

    # Cross-correlation vector rxd = E[x d*]
    rxd = (X.conj().T @ d_vec) / len(d_vec)

    # Solve Wiener–Hopf equations
    w = np.linalg.solve(Rxx, rxd)

    return w

def apply_fir_filter(x, h):
    """Apply FIR filter with coefficients h"""
    return np.convolve(x, h, mode="valid")
    
def apply_complex_fir_filter(x, h):
    """Apply complex FIR filter with coefficients h"""
    return np.convolve(x, h.conj(), mode="valid")    

def wiener_filter_frequency(X, Sdd, Svv):
    """
    Frequency-domain Wiener filter
    """
    H = Sdd / (Sdd + Svv)
    return H * X

class WienerFilter:
    def __init__(self):
        self.coefficients = []
    
    def create_filter(self, x, d, M):
        self.coefficients = complex_wiener_coefficients(x, d, M)
    
    def apply_filter(self, x):
        return np.convolve(x, self.coefficients, mode="valid")
        
    def process(self, x):
        return self.apply_filter(x)



if __name__ == "__main__":
    # Real Wiener filter
    np.random.seed(0)

    fs = 1000
    t = np.arange(0, 1, 1/fs)

    # Desired signal
    d = np.sin(2 * np.pi * 50 * t)

    # Noise
    v = 0.5 * np.random.randn(len(t))

    # Observed signal
    x = d + v
    
    M = 16  # filter length
    w = wiener_coefficients(x, d, M)

    print("Wiener coefficients:")
    print(w)
    
    y = apply_fir_filter(x, w)
    d_trim = d[M - 1:]

    # Mean square error
    mse = np.mean((d_trim - y)**2)
    print("MSE:", mse)
    
    # Complex Wiener filter
    np.random.seed(1)

    fs = 1000
    t = np.arange(0, 1, 1/fs)

    # Desired complex baseband signal
    d = np.exp(1j * 2 * np.pi * 50 * t)

    # Complex white noise
    noise = 0.5 * (np.random.randn(len(t)) + 1j * np.random.randn(len(t)))

    # Observed signal
    x = d + noise
    
    M = 16
    w = complex_wiener_coefficients(x, d, M)

    print("Complex Wiener coefficients:")
    print(w)
    
    y = apply_complex_fir(x, w)
    d_trim = d[M - 1:]

    mse = np.mean(np.abs(d_trim - y)**2)
    print("Mean squared error:", mse)
