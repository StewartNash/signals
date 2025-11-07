import numpy as np
import matplotlib.pyplot as plt

def plot_digital_response(poles,
        zeros,
        sampling_frequency,
        points=1000,
        is_mirrored=False,
        is_normalized=True,
        ylim=-60,
        xlim=0):
    Fs = sampling_frequency
    zeros = np.array(zeros, dtype=float)
    zeros = zeros[:, 0] + 1j * zeros[:, 1]
    poles = np.array(poles, dtype=float)
    poles = poles[:, 0] + 1j * poles[:, 1]

    if not is_mirrored:
        zeros = np.concatenate((zeros, np.conj(zeros)))
        poles = np.concatenate((poles, np.conj(poles)))

    #K = 1.0 # Gain
    gain = 1.0
    omega = np.linspace(0, np.pi, points)
    z = np.exp(1j * omega) # Frequency grid on unit circle (radians / sample)

    numerator = np.ones_like(z, dtype=complex)
    denominator = np.ones_like(z, dtype=complex)
    for zero in zeros:
        numerator *= (z - zero)
    for pole in poles:
        denominator *= (z - pole)

    H = gain * numerator / denominator
    if is_normalized: # Apply normalization
        H_dc = np.prod([(1 - zero) for zero in zeros]) / np.prod([(1 - pole) for pole in poles])
        H_nyquist = np.prod([(-1 - zero) for zero in zeros]) / np.prod([(-1 - pole) for pole in poles])
        # To choose normalization point assume higher magnitude is passband
        if abs(H_dc) >= abs(H_nyquist):
            gain = 1.0 / abs(H_dc)
        else:
            gain = 1.0 / abs(H_nyquist)
        H *= gain
    magnitude = np.abs(H)
    magnitude_decibels = 20 * np.log10(np.maximum(magnitude, 1e-12)) # Avoid -inf
    frequencies = omega * Fs / (2 * np.pi) # Hertz

    plt.figure(figsize=(8, 4))
    plt.plot(frequencies, magnitude_decibels)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    if (is_normalized):
        plt.title("Digital Frequency Response (Normalized)")
    else:
        plt.title("Digital Frequency Response")
    plt.grid(True)
    plt.ylim(ylim, None)
    plt.xlim(xlim, None)
    plt.show()
    
def plot_analog_response(poles,
        zeros,
        sampling_frequency,
        points=1000,
        is_mirrored=False,
        is_normalized=True,
        ylim=-60,
        xlim=0):
    Fs = sampling_frequency
    zeros = np.array(zeros, dtype=float)
    zeros = zeros[:, 0] + 1j * zeros[:, 1]
    poles = np.array(poles, dtype=float)
    poles = poles[:, 0] + 1j * poles[:, 1]

    if not is_mirrored:
        zeros = np.concatenate((zeros, np.conj(zeros)))
        poles = np.concatenate((poles, np.conj(poles)))

    #K = 1.0 # Gain
    gain = 1.0
    upper_range = points * np.pi # Choose range
    omega = np.linspace(0, upper_range, points) # radians per second
    s = 1j * omega

    numerator = np.ones_like(s, dtype=complex)
    denominator = np.ones_like(s, dtype=complex)
    for zero in zeros:
        numerator *= (z - zero)
    for pole in poles:
        denominator *= (z - pole)

    H = gain * numerator / denominator
    if is_normalized: # Apply normalization
        H0 = np.prod([-zero for zero in zeros]) / np.prod([-pole for pole in poles])
        gain = 1.0 / abs(H0)
        H *= gain
    magnitude = np.abs(H)
    magnitude_decibels = 20 * np.log10(np.maximum(magnitude, 1e-12)) # Avoid -inf
    frequencies = omega * Fs / (2 * np.pi) # Hertz

    plt.figure(figsize=(8, 4))
    plt.plot(frequencies, magnitude_decibels)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    if (is_normalized):
        plt.title("Analog Frequency Response (Normalized)")
    else:
        plt.title("Analog Frequency Response")
    plt.grid(True)
    plt.ylim(ylim, None)
    plt.xlim(xlim, None)
    plt.show()
    
    
