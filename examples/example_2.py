import numpy as np

from signal_processor.stochastic import WienerFilter
from signal_processor.stochastic import wiener_coefficients, complex_wiener_coefficients, apply_fir_filter, apply_complex_fir_filter

fs = 1000
t = np.arange(0, 1, 1/fs)

# Desired complex baseband signal
s = np.exp(1j * 2 * np.pi * 50 * t)

# Complex white noise
noise = 0.5 * (np.random.randn(len(t)) + 1j * np.random.randn(len(t)))

# Observed signal
x = s + noise

M = 16
h = complex_wiener_coefficients(x, s, M)

print("Complex Wiener coefficients:")
print(h)

y = apply_complex_fir_filter(x, h)
s_trim = s[M - 1:]

mse = np.mean(np.abs(s_trim - y)**2)
print("Mean squared error:", mse)


