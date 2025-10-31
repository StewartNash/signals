import math
import numpy as np
import matplotlib.pyplot as plt
from signal_processor.finite_impulse_response import kaiser_coefficients, kaiser_filter_order, kaiser_bandpass, magnitude_response
from signal_processor.filter import FilterType

#---------------------------------
# Example 5.6: Bandpass FIR Filter
#---------------------------------
# Design a bandpass filter with the following specifications
# Passband: fp1 = 120 Hz, fp2 = 180 Hz, Ap = 0.5 dB
# Stopband: fs1 = 60 Hz, fs2 = 240 Hz, As = 35 dB
# Sampling frequency (F) = 600 Hz

# Ripple parameter, delta = 0.0177828 (Eq. 5.49)
# Actual stopband attenuation, As = 35 dB (Eq. 5.44)
# Parameter D, D = 1.883705 (Eq. 5.50)
# Filter order, N = 21 (Eq. 5.51)
# Non-causal impulse response (Eqs. 5.60, 5.61, 5.39, 5.52)

FREQUENCY_RESOLUTION = 500

# Filter specifications
passband_frequency_low = 120
passband_frequency_high = 180
specified_passband_ripple = 0.5
stopband_frequency_low = 60
stopband_frequency_high = 240
minimum_stopband_attenuation = 35
sampling_frequency = 600

filter_type = FilterType.BANDPASS

filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(filter_type,
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
	
maximum_frequency = sampling_frequency / 2
frequencies = np.linspace(0, maximum_frequency, FREQUENCY_RESOLUTION)
angular_frequencies = frequencies * 2 * math.pi

response_magnitude = [magnitude_response(w, impulse_response, sampling_frequency, filter_order)
                      for w in angular_frequencies]
response_magnitude_db = [20 * math.log10(max(abs(m), 1e-10)) for m in response_magnitude]

# Plot
plt.figure(figsize=(8,4))
plt.plot(frequencies, response_magnitude_db)
plt.xlim(0, sampling_frequency / 2)
plt.ylim(-100, 5)
plt.axvline(stopband_frequency_low, color='red', linestyle='--', label='Stopband Low')
plt.axvline(passband_frequency_low, color='green', linestyle='--', label='Passband Low')
plt.axvline(passband_frequency_high, color='green', linestyle='--', label='Passband High')
plt.axvline(stopband_frequency_high, color='red', linestyle='--', label='Stopband High')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title(f"Kaiser Bandpass FIR (N={filter_order}, A={minimum_stopband_attenuation} dB)")
plt.grid(True)
plt.legend()
plt.show()

