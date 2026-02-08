import math
import numpy as np
import matplotlib.pyplot as plt
from signals.finite_impulse_response import kaiser_filter_order, kaiser_coefficients, kaiser_lowpass, magnitude_response
from signals.filter import FilterType

# -------------------------------
# Example 5.4: Lowpass FIR Filter
# -------------------------------
# Using the Kaiser window method, design an FIR lowpass digital filter with given specifications

FREQUENCY_RESOLUTION = 500

# Filter specifications
actual_passband_ripple = 0.1  # dB (less than)
minimum_stopband_attenuation = 44  # dB (greater than)
passband_frequency = 500  # Hz
stopband_frequency = 750  # Hz
sampling_frequency = 2500  # Hz

filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(
    filter_type=FilterType.LOWPASS,
    passband_frequency_low=passband_frequency,
    passband_frequency_high=passband_frequency,
    stopband_frequency_low=stopband_frequency,
    stopband_frequency_high=stopband_frequency,
    sampling_frequency=sampling_frequency,
    specified_passband_ripple=actual_passband_ripple,
    minimum_stopband_attenuation=minimum_stopband_attenuation)                                        
                    
kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)
impulse_response = kaiser_lowpass(passband_frequency,
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
plt.title(f"Kaiser Lowpass FIR (N={filter_order}, A={minimum_stopband_attenuation} dB)")
plt.grid(True)
plt.legend()
plt.show()

