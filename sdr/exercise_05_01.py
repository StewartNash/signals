import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Set parameters
# -------------------------
fs = 10240                  # sampling rate (Hz)
T_max = 1.0                 # simulation end time (s)
t = np.arange(0, T_max, 1/fs)  # time vector

f1 = 100                    # frequency of 1st tone (Hz)
f2 = 200                    # frequency of 2nd tone (Hz)
f3 = 300                    # frequency of 3rd tone (Hz)

A1 = 10                     # amplitudes
A2 = 1
A3 = 4

# -------------------------
# Create sum of cosines
# -------------------------
s_t = (
    A1 * np.cos(2 * np.pi * f1 * t) +
    A2 * np.cos(2 * np.pi * f2 * t) +
    A3 * np.cos(2 * np.pi * f3 * t)
)

# -------------------------
# FFT (rectangular window)
# -------------------------
Nfft = 1024
#X_1 = (1 / (2 * fs)) * np.fft.fft(s_t, Nfft)
X_1 = np.fft.fft(s_t, Nfft) / len(s_t)
f = np.arange(0, Nfft) / Nfft * fs

magnitude = np.abs(X_1)
phase = np.angle(X_1)
threshold = 1E-6
phase = np.where(magnitude > threshold, phase, np.nan)
#magnitude = np.where(magnitude > threshold, magnitude, np.nan)
magnitude_db = 20 * np.log10(np.maximum(magnitude, threshold))
magnitude_db = np.where(magnitude > threshold, magnitude_db, np.nan)

# -------------------------
# Plot time-domain waveform
# -------------------------
plt.figure(201)
plt.plot(t, s_t, 'b-', linewidth=2)
plt.axis([0, 0.03, -20, 20])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.title('Sum of Cosines')
plt.grid(True)

# -------------------------
# Plot FFT magnitude
# -------------------------
plt.figure(202)
plt.stem(
    f,
    magnitude_db, #20 * np.abs(X_1),
    linefmt='r-',
    markerfmt='ro',
    basefmt=' '
)
plt.axis([0, 400, -30, 0])
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude (dB)')
plt.title('FFT with rectangular window')
plt.grid(True)

# -------------------------
# Plot FFT phase
# -------------------------
plt.figure(203)
plt.stem(
    f,
    phase, #np.angle(X_1),
    linefmt='g-',
    markerfmt='go',
    basefmt=' '
)
plt.axis([0, 400, -np.pi, np.pi])
plt.xlabel('frequency (Hz)')
plt.ylabel('phase (radians)')
plt.title('FFT Phase Spectrum')
plt.grid(True)

plt.show()
