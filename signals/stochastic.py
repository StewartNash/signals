import numpy as np

def wiener_coefficients(x, s, M):
    """
    Compute Wiener filter coefficients
    
    x : noisy input signal
    s : desired signal
    M : filter length
    """
    N = len(x)
    
    X = np.zeros((N - M + 1, M))
    for i in range(M): # Build data matrix
        X[:, i] = x[M - 1 - i : N - i]
    s_vector = s[M - 1:]
    
    #Rxx = (X.T @ X) / len(s_vector) # Autocorrelation matrix
    T = (X.T @ X) / len(s_vector) # Autocorrelation matrix
    v = (X.T @ s_vector) / len(s_vector) # Cross-correlation vector
    #h = np.linalg.solve(Rxx, v) # Solve Wiener–Hopf equations
    h = np.linalg.solve(T, v) # Solve Wiener–Hopf equations
    
    return h

#def complex_wiener_coefficients(x, signal_vector, epsilon=1E-6)
def complex_wiener_coefficients(x, s, M, epsilon=1E-6):
    """
    Compute complex Wiener filter coefficients
    
    x : complex noisy input signal
    s : complex desired signal
    M : filter length
    """
    x = np.asarray(x, dtype=np.complex128)
    s = np.asarray(s, dtype=np.complex128)

    N = len(x)
    if len(s) != N:
        raise ValueError("x and s must have the same length")

    X = np.zeros((N - M + 1, M), dtype=np.complex128) # Data matrix
    for i in range(M):
        X[:, i] = x[M - 1 - i : N - i]
    s_vector = s[M - 1:]
    
    #Rxx = (X.conj().T @ X) / len(s_vector) # Autocorrelation matrix
    T = (X.conj().T @ X) / len(s_vector) # Autocorrelation matrix
    Rxs = (X.conj().T @ s_vector) / len(s_vector) # Cross-correlation vector
    #Rxx += epsilon * np.eye(M) # diagonal loading
    T += epsilon * np.eye(M) # diagonal loading
    #h = np.linalg.solve(Rxx, Rxs) # Solve Wiener–Hopf equations
    h = np.linalg.solve(T, Rxs) # Solve Wiener–Hopf equations

    return h

def apply_fir_filter(x, h):
    """Apply FIR filter with coefficients h"""
    return np.convolve(x, h, mode="valid")
    
def apply_complex_fir_filter(x, h):
    """Apply complex FIR filter with coefficients h"""
    return np.convolve(x, h, mode="valid")

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
        

class JCLMSFilter:
    """
    JCLMS filter
    Joint Complex LMS (least mean squares)
    Joint complex gradient transversal filter    
    """
    def __init__(self, order, mu):
        self.order = order
        self.mu = mu

        # Weight vectors
        self.w = np.zeros(order, dtype=np.complex128)
        self.g = np.zeros(order, dtype=np.complex128)

        # Input buffer
        self.x = np.zeros(order, dtype=np.complex128)

    def process(self, sample, desired):
        """
        Process one complex sample and update weights
        """
        # Shift buffer
        self.x[1:] = self.x[:-1]
        self.x[0] = sample

        # Filter output (widely linear model)
        y = np.vdot(self.w, self.x) + np.vdot(self.g, np.conj(self.x))

        # Error
        e = desired - y

        # Weight updates
        self.w += self.mu * np.conj(e) * self.x
        self.g += self.mu * np.conj(e) * np.conj(self.x)

        return y, e

if __name__ == "__main__":
    # Complex Wiener filter
    np.random.seed(0)
    fs = 1000
    t = np.arange(0, 1, 1 / fs)
    s = np.exp(1j * 2 * np.pi * 50 * t) # Desired complex baseband signal
    noise = 0.15 * (np.random.randn(len(t)) + 0.15j * np.random.randn(len(t))) # Complex white noise
    x = s + noise # Observed signal
    M = 16 # Filter length
    h = complex_wiener_coefficients(x, s, M)
    print("Complex Wiener coefficients:")
    print(h)
    y = apply_complex_fir_filter(x, h)
    s_trimmed = s[M - 1:]
    mse = np.mean(np.abs(s_trimmed - y)**2)
    print("Mean squared error: ", mse)

    xx = x[M - 1:].real
    yy = y.real
    ss = s_trimmed.real
    nn = list(range(1, len(yy) + 1))

    #plt.scatter(nn, xx, label="Noisy input - real", marker='o')
    #plt.scatter(nn, yy, label="Filter response - real", marker='o')
    #plt.scatter(nn, ss, label="Desired signal - real", marker='o')
    plt.plot(nn, xx, label="Noisy input - real", marker='o')
    plt.plot(nn, yy, label="Filter response - real", marker='o')
    plt.plot(nn, ss, label="Desired signal - real", marker='o')
    plt.grid()
    plt.xlabel("Input sequence number")
    plt.ylabel("Value")
    plt.legend()
    plt.title("Complex Wiener Filter")
    plt.show()

    # Real Wiener filter
    np.random.seed(1)
    fs = 1000
    t = np.arange(0, 1, 1 / fs)
    s = np.sin(2 * np.pi * 50 * t) # Desired signal
    noise = 0.15 * np.random.randn(len(t))
    x = s + noise # Observed signal
    M = 16  # Filter length
    h = wiener_coefficients(x, s, M)
    print("Real Wiener coefficients:")
    print(h)
    y = apply_fir_filter(x, h)
    s_trimmed = s[M - 1:]
    mse = np.mean((s_trimmed - y)**2) # Mean square error
    print("MSE: ", mse)

    xx = x[M - 1:].real
    yy = y.real
    ss = s_trimmed.real
    nn = list(range(1, len(yy) + 1))

    #plt.scatter(nn, xx, label="Noisy input - real", marker='o')
    #plt.scatter(nn, yy, label="Filter response - real", marker='o')
    #plt.scatter(nn, ss, label="Desired signal - real", marker='o')
    plt.plot(nn, xx, label="Noisy input - real", marker='o')
    plt.plot(nn, yy, label="Filter response - real", marker='o')
    plt.plot(nn, ss, label="Desired signal - real", marker='o')
    plt.grid()
    plt.xlabel("Input sequence number")
    plt.ylabel("Value")
    plt.legend()
    plt.title("Real Wiener Filter")
    plt.show()
