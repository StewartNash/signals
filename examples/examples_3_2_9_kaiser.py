import math
import numpy as np
import matplotlib.pyplot as plt
import enum

# ---------------------------
# Filter Types
# ---------------------------
class FilterType(enum.Enum):
    LOWPASS = 1
    HIGHPASS = 2
    BANDPASS = 3
    BANDSTOP = 4

# ---------------------------
# Kaiser Window Coefficients
# ---------------------------
def zo_mod_bessel_fk(x, N=25):
    """Approximation of I0(x) using series expansion."""
    output = 0
    for i in range(N + 1):
        output += ((x / 2) ** i / math.factorial(i)) ** 2
    return output

def kaiser_coefficients(filter_order, minimum_stopband_attenuation):
    n = filter_order
    if minimum_stopband_attenuation <= 21.0:
        alpha = 0
    elif minimum_stopband_attenuation <= 50.0:
        alpha = 0.5842 * (minimum_stopband_attenuation - 21) ** 0.4 + \
                0.07886 * (minimum_stopband_attenuation - 21)
    else:
        alpha = 0.1102 * (minimum_stopband_attenuation - 8.7)

    kaiser_coeffs = np.zeros(n)
    I0_alpha = zo_mod_bessel_fk(alpha, 31)
    for i in range(n):
        ratio = (2 * i / (n - 1)) - 1.0
        beta = alpha * math.sqrt(1 - ratio ** 2)
        kaiser_coeffs[i] = zo_mod_bessel_fk(beta, 31) / I0_alpha

    return kaiser_coeffs, alpha

# ---------------------------
# Kaiser Filter Order
# ---------------------------
def kaiser_filter_order(filter_type,
    passband_frequency_low,
    passband_frequency_high,
    stopband_frequency_low,
    stopband_frequency_high,
    sampling_frequency,
    specified_passband_ripple,
    minimum_stopband_attenuation):

    transition_bandwidth_low  = abs(passband_frequency_high - stopband_frequency_high)
    transition_bandwidth_high = abs(passband_frequency_low - stopband_frequency_low)

    if filter_type == FilterType.LOWPASS:
        transition_bandwidth = transition_bandwidth_low
    elif filter_type == FilterType.HIGHPASS:
        transition_bandwidth = transition_bandwidth_high
    elif filter_type in (FilterType.BANDPASS, FilterType.BANDSTOP):
        transition_bandwidth = min(transition_bandwidth_low, transition_bandwidth_high)
    else:
        raise ValueError("Unsupported filter type")

    delta_stopband = 10 ** (-0.05 * minimum_stopband_attenuation)
    delta_passband = (10 ** (0.05 * specified_passband_ripple) - 1) / \
                     (10 ** (0.05 * specified_passband_ripple) + 1)
    delta = min(delta_passband, delta_stopband)
    minimum_stopband_attenuation = -20 * math.log10(delta)

    if minimum_stopband_attenuation <= 21:
        parameter_d = 0.9222
    else:
        parameter_d = (minimum_stopband_attenuation - 7.95) / 14.36

    filter_order = int(2 + parameter_d * sampling_frequency / transition_bandwidth)
    if filter_order % 2 == 0:
        filter_order += 1  # Make it odd for symmetry

    return filter_order, delta, minimum_stopband_attenuation, parameter_d

# ---------------------------
# Corrected Bandpass Design
# ---------------------------
def kaiser_bandpass(fp1, fp2, fs1, fs2, fs, N, kaiser_coeffs):
    # Transition midpoint to define cutoff edges
    delta_f_1 = fp1 - fs1
    delta_f_h = fs2 - fp2
    delta_f = min(delta_f_1, delta_f_h)
    fc1 = fp1 - delta_f/2
    fc2 = fp2 + delta_f/2

    M = N - 1
    n = np.arange(N)

    # Ideal bandpass: difference of two lowpass filters (centered)
    h_ideal = (2 * fc2 / fs) * np.sinc(2 * fc2 * (n - M/2) / fs) \
            - (2 * fc1 / fs) * np.sinc(2 * fc1 * (n - M/2) / fs)

    # Apply Kaiser window
    h = h_ideal * kaiser_coeffs

    # ---- Passband normalization at center frequency ----
    fc_mid = 0.5 * (fp1 + fp2)
    omega = 2 * math.pi * fc_mid / fs
    re = 0.0
    im = 0.0
    for k in range(N):
        re += h[k] * math.cos(omega * k)
        im -= h[k] * math.sin(omega * k)
    gain = math.sqrt(re*re + im*im)
    h /= gain

    return h

# ---------------------------
# Frequency Response (manual)
# ---------------------------
def magnitude_response(impulse_response, frequencies, sampling_frequency):
    N = len(impulse_response)
    response_mag = []
    for f in frequencies:
        omega = 2 * math.pi * f / sampling_frequency
        re = 0.0
        im = 0.0
        for n in range(N):
            re += impulse_response[n] * math.cos(omega * n)
            im -= impulse_response[n] * math.sin(omega * n)
        mag = math.sqrt(re*re + im*im)
        response_mag.append(mag)
    return np.array(response_mag)

# ---------------------------
# Example Usage
# ---------------------------
if __name__ == "__main__":
    # Filter specifications
    passband_frequency_low = 120
    passband_frequency_high = 180
    specified_passband_ripple = 0.5   # dB
    stopband_frequency_low = 60
    stopband_frequency_high = 240
    minimum_stopband_attenuation = 35  # dB
    sampling_frequency = 600

    filter_type = FilterType.BANDPASS

    filter_order, delta, minimum_stopband_attenuation, parameter_d = \
        kaiser_filter_order(filter_type,
            passband_frequency_low,
            passband_frequency_high,
            stopband_frequency_low,
            stopband_frequency_high,
            sampling_frequency,
            specified_passband_ripple,
            minimum_stopband_attenuation)

    kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)

    impulse_response = kaiser_bandpass(passband_frequency_low,
        passband_frequency_high,
        stopband_frequency_low,
        stopband_frequency_high,
        sampling_frequency,
        filter_order,
        kaiser_coeffs)

    # Frequency response
    FREQUENCY_RESOLUTION = 500
    maximum_frequency = sampling_frequency / 2
    frequencies = np.linspace(0, maximum_frequency, FREQUENCY_RESOLUTION)

    response_magnitude = magnitude_response(impulse_response, frequencies, sampling_frequency)
    response_magnitude_db = 20 * np.log10(np.maximum(response_magnitude, 1e-10))

    # Plot
    plt.figure(figsize=(8,4))
    plt.plot(frequencies, response_magnitude_db)
    plt.xlim(0, sampling_frequency / 2)
    plt.ylim(-80, 5)
    plt.axvline(passband_frequency_low, color='green', linestyle='--', label='Passband Low')
    plt.axvline(passband_frequency_high, color='green', linestyle='--', label='Passband High')
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title(f"Kaiser Bandpass FIR (N={filter_order}, A={minimum_stopband_attenuation:.1f} dB)")
    plt.grid(True)
    plt.legend()
    plt.show()
