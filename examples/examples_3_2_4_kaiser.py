import math
import numpy as np
import matplotlib.pyplot as plt
from signal_processor.finite_impulse_response import kaiser_coefficients, kaiser_filter_order, kaiser_bandstop, magnitude_response
from signal_processor.filter import FilterType

#-----------------------------------
# Problem 5.3.9: Bandstop FIR Filter
#-----------------------------------
# Write a computer program to design a Kaiser window
# FIR bandstop digital filter satisfying the following
# specifications
#
# fp1 = 100 Hz
# fp2 = 700 Hz
# fs1 = 200 Hz
# fs2 = 400 Hz
# F = 3000 Hz
# Ap = 0.3 dB
# As = 35 dB

FREQUENCY_RESOLUTION = 500

# Filter specifications
passband_frequency_low = 100
passband_frequency_high = 700
specified_passband_ripple = 0.3
stopband_frequency_low = 200
stopband_frequency_high = 400
minimum_stopband_attenuation = 35
sampling_frequency = 3000

filter_type = FilterType.BANDSTOP

filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	specified_passband_ripple,
	minimum_stopband_attenuation)

kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)

impulse_response = kaiser_bandstop(passband_frequency_low,
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
plt.title(f"Kaiser Bandstop FIR (N={filter_order}, A={minimum_stopband_attenuation} dB)")
plt.grid(True)
plt.legend()
plt.show()
