import numpy as np

def wiener_coefficients(x, d, M):
    """
    Compute Wiener filter coefficients
    
    x : noisy input signal
    d : desired signal
    M : filter length
    """
    N = len(x)
    
    # Build data matrix
    X = np.zeros((N - M + 1, M))
    for i in range(M):
        X[:, i] = x[M - 1 - i : N - i]

    d_vec = d[M - 1:]

    # Autocorrelation matrix
    Rxx = (X.T @ X) / len(d_vec)

    # Cross-correlation vector
    rxd = (X.T @ d_vec) / len(d_vec)

    # Wiener solution
    w = np.linalg.solve(Rxx, rxd)
    
    return w
    
def apply_fir_filter(x, w):
    """Apply FIR filter with coefficients w"""
    return np.convolve(x, w, mode="valid")
    

def wiener_filter_frequency(X, Sdd, Svv):
    """
    Frequency-domain Wiener filter
    """
    H = Sdd / (Sdd + Svv)
    return H * X

if __main__():
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
