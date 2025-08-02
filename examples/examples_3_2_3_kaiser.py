import math
import numpy as np
import matplotlib.pyplot as plt
from signal_processor.finite_impulse_response import kaiser_filter_order, kaiser_coefficients, kaiser_highpass, magnitude_response, FilterType

# ----------------------------------
# Problem 5.3.7: Highpass FIR Filter
# ----------------------------------
# Write a computer program to design a Kaiser window
# FIR highpass digital filter satisfying the following
# specifications
#
# fp = 3200 Hz
# fs = 1600 Hz
# F = 10000 Hz
# Ap = 0.1 dB
# As = 40 dB

FREQUENCY_RESOLUTION = 1000

# Filter specifications
actual_passband_ripple = 0.1  # dB (less than)
minimum_stopband_attenuation = 40  # dB (greater than)
passband_frequency = 3200  # Hz
stopband_frequency = 1600  # Hz
sampling_frequency = 10000  # Hz

filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(
	filter_type=FilterType.HIGHPASS,
	passband_frequency_low=passband_frequency,
	passband_frequency_high=passband_frequency,
	stopband_frequency_low=stopband_frequency,
	stopband_frequency_high=stopband_frequency,
	sampling_frequency=sampling_frequency,
	specified_passband_ripple=actual_passband_ripple,
	minimum_stopband_attenuation=minimum_stopband_attenuation)										  
					
kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)
impulse_response = kaiser_highpass(passband_frequency,
	stopband_frequency,
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
plt.axvline(passband_frequency, color='green', linestyle='--', label='Passband Edge')
plt.axvline(stopband_frequency, color='red', linestyle='--', label='Stopband Start')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title(f"Kaiser Highpass FIR (N={filter_order}, A={minimum_stopband_attenuation} dB)")
plt.grid(True)
plt.legend()
plt.show()
