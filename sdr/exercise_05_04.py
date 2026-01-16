import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Set parameters
# -------------------------
fs = 10240                      # sampling rate (Hz)
T_max = 1.0                     # simulation end time (s)
t = np.arange(0, T_max, 1/fs)   # time vector

f1 = 100                        # frequencies (Hz)
f2 = 200
f3 = 300

A1 = 10                         # amplitudes
A2 = 1
A3 = 4

# -------------------------
# Create sum of cosines (with phase offsets)
# -------------------------
s_t = (
    A1 * np.cos(2 * np.pi * f1 * t + np.pi / 4) +
    A2 * np.cos(2 * np.pi * f2 * t + np.pi / 6) +
    A3 * np.cos(2 * np.pi * f3 * t)
)

# -------------------------
# Add small impulse (phase reference)
# -------------------------
r_t = np.zeros_like(s_t)
r_t[0] = 0.01                   # try commenting out to see phase ambiguity
y_t = s_t + r_t

# -------------------------
# FFT (rectangular window)
# -------------------------
Nfft = 1024

X_1 = np.fft.fftshift(np.fft.fft(y_t, Nfft)) / (2 * fs)

f = (np.arange(-Nfft//2, Nfft//2) / Nfft) * fs

# -------------------------
# Time-domain plot
# -------------------------
plt.figure(501)
plt.plot(t, s_t, linewidth=2, color=(0.2, 0.7, 0.2))
plt.axis([0, 0.05, -15, 15])
plt.xlabel("time (s)")
plt.ylabel("amplitude")
plt.grid(True)

# -------------------------
# Magnitude spectrum (2-sided)
# -------------------------
m = np.abs(X_1)

plt.figure(502)
plt.stem(f, 20 * m, linefmt='-', markerfmt='o', basefmt=' ')
plt.axis([-500, 500, 0, 11])
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.title("Complex magnitude spectrum")
plt.grid(True)

# -------------------------
# Phase spectrum
# -------------------------
g = np.mod(np.angle(X_1), np.pi)

plt.figure(503)
plt.stem(f, g, linefmt='-', markerfmt='o', basefmt=' ')
plt.axis([0, 500, 0, np.pi])
plt.xlabel("frequency (Hz)")
plt.ylabel("phase (radians)")
plt.title("Phase spectrum")
plt.grid(True)

# -------------------------
# Significant components
# -------------------------
idx = np.where(m > 0.01)[0]

# -------------------------
# Real and Imaginary parts (significant bins only)
# -------------------------
plt.figure(504)

plt.subplot(2, 1, 1)
plt.stem(f[idx], 20 * np.real(X_1[idx]), linefmt='r-', markerfmt='ro', basefmt=' ')
plt.axis([-500, 500, -10, 10])
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.title("Magnitude FFT (REAL part, significant components only)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(f[idx], 20 * np.imag(X_1[idx]), linefmt='b-', markerfmt='bo', basefmt=' ')
plt.axis([-500, 500, -10, 10])
plt.xlabel("frequency (Hz)")
plt.ylabel("magnitude")
plt.title("Magnitude FFT (IMAGINARY part, significant components only)")
plt.grid(True)

plt.tight_layout()
plt.show()

