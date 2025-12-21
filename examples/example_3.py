import numpy as np
import matplotlib.pyplot as plt

"""
Using a JCLMS filter we generate a waterfall plot (showing power in dB versus the spectrum) of the filter output where there is a primary channel and a reference channel which have the following characteristics,
Reference channel:
(1) Dual constant angular frequency sinusoids, omega_1 and omega_2 with a sampling frequency of f_0
(2) snr_1 (signal-to-noise ratio of omega_1) is 20 dB
(3) snr_2 (signal-to-noise ratio of omega_2) is 10 dB
(4) both signals undergo an instantaneous downward step in frequency with the following characteristics
	(a) omega_1 before the shift is (f_0 * 7 * PI / 8)
	(b) The change in omega_1 is (-f_0 * PI / 8)
	(c) omega_2 before the shift is (f_0 * PI / 4)
	(d) The change in omega_2 is (-f_0 * PI / 8)
	(e) The shift occurs at no less than halfway through sampling
Primary channel:
(1) Dual constant angular frequency sinusoids, omega_3 and omega_4
(2) snr_3 (signal-to-noise ratio of omega_3) is 20 dB
(3) snr_4 (signal-to-noise ratio of omega_4) is 20 dB
(4) omega_3 is (f_0 * 3 * PI / 4)
(5) omega_4 is (f_0 * PI / 8)

We also generate a line plot of the prediction error over time in dB.
"""

# ============================================================
# JCLMS FILTER
# ============================================================
class JCLMSFilter:
    def __init__(self, order, mu):
        self.order = order
        self.mu = mu
        self.w = np.zeros(order, dtype=np.complex128)
        self.g = np.zeros(order, dtype=np.complex128)
        self.xbuf = np.zeros(order, dtype=np.complex128)

    def step(self, x, d):
        # Shift input buffer
        self.xbuf[1:] = self.xbuf[:-1]
        self.xbuf[0] = x

        # Widely-linear output
        y = np.vdot(self.w, self.xbuf) + np.vdot(self.g, np.conj(self.xbuf))

        # Error
        e = d - y

        # Weight update
        self.w += self.mu * np.conj(e) * self.xbuf
        self.g += self.mu * np.conj(e) * np.conj(self.xbuf)

        return y, e


# ============================================================
# SIGNAL PARAMETERS
# ============================================================
fs = 2000.0          # sampling frequency
N = 4096             # number of samples
t = np.arange(N) / fs
half = N // 2

# ============================================================
# REFERENCE CHANNEL (INTERFERENCE)
# ============================================================
# Angular frequencies specified in the problem
omega1_before = 7 * np.pi / 8
omega1_after  = 6 * np.pi / 8
omega2_before = np.pi / 4
omega2_after  = np.pi / 8

def complex_noise(snr_db, N):
    snr = 10**(snr_db / 10)
    noise_power = 1 / snr
    return np.sqrt(noise_power / 2) * (
        np.random.randn(N) + 1j * np.random.randn(N)
    )

ref = np.zeros(N, dtype=complex)

ref[:half] = (
    np.exp(1j * omega1_before * np.arange(half)) +
    np.exp(1j * omega2_before * np.arange(half))
)

ref[half:] = (
    np.exp(1j * omega1_after * np.arange(half)) +
    np.exp(1j * omega2_after * np.arange(half))
)

# Add noise with different SNRs
ref += complex_noise(20, N) + complex_noise(10, N)


# ============================================================
# PRIMARY CHANNEL (SIGNAL + CORRELATED INTERFERENCE)
# ============================================================
omega3 = 3 * np.pi / 4
omega4 = np.pi / 8

primary_signal = (
    np.exp(1j * omega3 * np.arange(N)) +
    np.exp(1j * omega4 * np.arange(N))
)

# Correlated interference from reference channel
primary = primary_signal + 0.8 * ref


# ============================================================
# RUN JCLMS ADAPTIVE FILTER
# ============================================================
order = 8
mu = 0.001

jclms = JCLMSFilter(order, mu)

y = np.zeros(N, dtype=complex)
e = np.zeros(N, dtype=complex)

for n in range(N):
    y[n], e[n] = jclms.step(ref[n], primary[n])


# ============================================================
# WATERFALL / SPECTROGRAM
# ============================================================
plt.figure(figsize=(10, 5))
plt.specgram(
    e,
    NFFT=256,
    Fs=fs,
    noverlap=192,
    scale="dB",
    cmap="viridis"
)
plt.colorbar(label="Power (dB)")
plt.title("JCLMS Prediction Error Spectrogram (Waterfall)")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()


# ============================================================
# PREDICTION ERROR POWER (dB)
# ============================================================
error_power_db = 10 * np.log10(np.abs(e)**2 + 1e-12)

plt.figure(figsize=(10, 4))
plt.plot(error_power_db)
plt.title("Prediction Error Power vs Time (dB)")
plt.xlabel("Sample Index")
plt.ylabel("Power (dB)")
plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================================
# COMPLEX WIENER FILTER (FIXED)
# ============================================================
def complex_wiener_coefficients(x, d, M, eps=1e-6):
    x = np.asarray(x, dtype=np.complex128)
    d = np.asarray(d, dtype=np.complex128)

    N = len(x)
    X = np.zeros((N - M + 1, M), dtype=np.complex128)
    for i in range(M):
        X[:, i] = x[M - 1 - i : N - i]

    d_vec = d[M - 1:]

    Rxx = (X.conj().T @ X) / len(d_vec)
    Rxx += eps * np.eye(M)  # diagonal loading

    rxd = (X.conj().T @ d_vec) / len(d_vec)

    return np.linalg.solve(Rxx, rxd)


def apply_complex_fir(x, h):
    return np.convolve(x, h, mode="valid")


# Compute Wiener filter ONCE
order = 8
h_wiener = complex_wiener_coefficients(ref, primary, order)

# Apply filter (fixed coefficients)
y = apply_complex_fir(ref, h_wiener)

# Prediction error (what remains after cancellation)
e = primary[order - 1:] - y


# ============================================================
# WATERFALL / SPECTROGRAM
# ============================================================
plt.figure(figsize=(10, 5))
plt.specgram(
    e,
    NFFT=256,
    Fs=fs,
    noverlap=192,
    scale="dB",
    cmap="viridis"
)
plt.colorbar(label="Power (dB)")
plt.title("Fixed Wiener Filter Output Spectrogram (No Tracking)")
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.tight_layout()
plt.show()

