import math
import random
import matplotlib.pyplot as plt

from signal_processor.filter import FilterFamily, FilterType
from signal_processor.finite_impulse_response import FIRFilter
from signal_processor.fourier_transform import discrete_fourier_transform

def signal_generator(fs, f_signal):
    t = 0
    while True:
        time = t / fs
        signal = math.sin(2 * math.pi * f_signal * time)
        noise = 0.3 * random.uniform(-1, 1)
        yield signal + noise
        t += 1

def white_noise_generator():
    while True:
        yield random.gauss(0.0, 1.0)


def compute_dft(signal):
    N = len(signal)
    X = []
    for k in range(N):
        Xk = discrete_fourier_transform(signal, k, N)
        X.append(Xk)
    return X


def compute_psd(signal, fs):
    N = len(signal)
    X = compute_dft(signal)

    # Keep only positive frequencies
    half = N // 2
    X = X[:half]

    psd = []
    freqs = []

    for k in range(half):
        mag2 = (X[k].real**2 + X[k].imag**2)
        power = mag2 / N
        psd.append(10 * math.log10(power + 1e-12))
        freqs.append(k * fs / N)

    return freqs, psd

# -------------------------------
# Example 5.4: Lowpass FIR Filter
# -------------------------------
# Using the Kaiser window method, design an FIR lowpass digital filter with given specifications

# Filter specifications
actual_passband_ripple = 0.1  # dB (less than)
minimum_stopband_attenuation = 44  # dB (greater than)
passband_frequency = 500  # Hz
stopband_frequency = 750  # Hz
sampling_frequency = 2500  # Hz

myFilter = FIRFilter()
myFilter.create_filter(
    filter_family=FilterFamily.CHEBYSHEV,
    filter_type=FilterType.LOWPASS,
    passband_frequency_low=passband_frequency,
    passband_frequency_high=passband_frequency,
    stopband_frequency_low=stopband_frequency,
    stopband_frequency_high=stopband_frequency,
    sampling_frequency=sampling_frequency,
    specified_passband_ripple=actual_passband_ripple,
    minimum_stopband_attenuation=minimum_stopband_attenuation)

# Simulated live signal
#gen = live_signal_generator(sampling_frequency, 300)  # 300 Hz test tone

# Process live samples
#filtered = []

#for _ in range(500):
#    x = next(gen)
#    y = fir.process(x)
#    filtered.append(y)

N = 512
Fs = sampling_frequency

gen = white_noise_generator()

raw = []
filtered = []

for _ in range(N):
    x = next(gen)
    y = myFilter.process(x)
    raw.append(x)
    filtered.append(y)

f_raw, psd_raw = compute_psd(raw, Fs)
f_filt, psd_filt = compute_psd(filtered, Fs)

plt.figure()
plt.plot(f_raw, psd_raw, label="Input White Noise")
plt.plot(f_filt, psd_filt, label="Filtered Output")
plt.xlabel("Frequency (Hz)")
plt.ylabel("PSD (dB)")
plt.title("DFT-Based PSD (Manual DFT)")
plt.legend()
plt.grid(True)
plt.show()
