import numpy as np
import matplotlib.pyplot as plt

from signals.stochastic import WienerFilter
from signals.stochastic import complex_wiener_coefficients, apply_complex_fir_filter
from signals.stochastic import wiener_coefficients, apply_fir_filter

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
