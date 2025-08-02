import math
import numpy as np
import matplotlib.pyplot as plt
from signal_processor.finite_impulse_response import kaiser_coefficients, kaiser_filter_order, kaiser_bandpass, magnitude_response, FilterType

# filter_order			nk, NK
# passband_frequency		fp
# passband_frequency_low	fp1, FP1
# passband_frequency_high	fp2, FP2
# stopband_frequency		fs, FS, f, F
# sampling_frequency		fs, FS, f, F (CORRECTION)
# stopband_frequency_low	fs1, fa1, FA1
# stopband_frequency_high	fs2, fa2, FA2
# transition_bandwidth_low	bt1
# transition_bandwidth_high	bt2
# transition_bandwidth		bt
# delta				_del
# delta_passband (ripple)	d1
# delta_stopband (ripple)	d2
# actual_passband_ripple	aap
# specified_passband_ripple	ap
# actual_stopband_attenuation	actual_minimum_stopband_attenuation
# minimum_stopband_attenuation	specified_minimum_stopband_attenuation
# minimum_stopband_attenuation	aa
# parameter_d			pard
# alpha				alp, ALP

# actual_passband_ripple	aa (CORRECTION)
# minimum_stopband_attenuation	aap (CORRECTION)
# kaiser_coeffs			wk, WK
# mod_bessel_fk_alpha		modified_bessel_first_kind_alpha
# mod_bessel_fk_beta		modified_bessel_first_kind_beta
# mod_bessel_fk_alpha		IOALP
# mod_bessel_fk_beta		IOBE
# beta				BE
#				KFAC (factorial)
# cutoff_frequency		wc, WC
# cutoff_frequency_low		wc1, WC1
# cutoff_frequency_high		wc2, WC2
# initial_impulse_response	H1
# impulse_response		H
# sinc_function			fnsx, FNSX
# argument			ARG

# Example 5.6
# Design a bandpass filter with the following specifications
# Passband: fp1 = 120 Hz, fp2 = 180 Hz, Ap = 0.5 dB
# Stopband: fs1 = 60 Hz, fs2 = 240 Hz, As = 35 dB
# Sampling frequency (F) = 600 Hz

# Ripple parameter, delta = 0.0177828 (Eq. 5.49)
# Actual stopband attenuation, As = 35 dB (Eq. 5.44)
# Parameter D, D = 1.883705 (Eq. 5.50)
# Filter order, N = 21 (Eq. 5.51)
# Non-causal impulse response (Eqs. 5.60, 5.61, 5.39, 5.52)

# (causal index, non-causal index, hd[n], ak[n], ak[n]hd[n])

fir_coefficients = [
	( 0, -10,  0.000000000, 0.243827427,  0.000000000),
	( 1,  -9, -0.000000000, 0.342116577,  0.000000000),
	( 2,  -8, -0.075682673, 0.445786231, -0.033738293),
	( 3,  -7,  0.000000000, 0.550960881,  0.000000000),
	( 4,  -6,  0.062365952, 0.653488069,  0.040755406),
	( 5,  -5,  0.000000000, 0.749153304,  0.000000000),
	( 6,  -4,  0.093548928, 0.833903592,  0.078010787),
	( 7,  -3, -0.000000000, 0.904066210,  0.000000000),
	( 8,  -2, -0.302730691, 0.956549514, -0.289576896),
	( 9,  -1,  0.000000000, 0.989013547,  0.000000000),
	(10,   0,  0.400000000, 1.000000000,  0.400000000),
	(11,   1,  0.000000000, 0.989013547,  0.000000000),
	(12,   2, -0.302730691, 0.956549514, -0.289576896),
	(13,   3, -0.000000000, 0.904066210,  0.000000000),
	(14,   4,  0.093548928, 0.833903592,  0.078010787),
	(15,   5,  0.000000000, 0.749153304,  0.000000000),
	(16,   6,  0.062365952, 0.653488069,  0.040755406),
	(17,   7,  0.000000000, 0.550960881,  0.000000000),
	(18,   8, -0.075682673, 0.445786231, -0.033738293),
	(19,   9, -0.000000000, 0.342116577,  0.000000000),
	(20,  10,  0.000000000, 0.243827427,  0.000000000),
]

# (frequency, response)

frequency_response = [
	(0.000, -40.95871194),
	(0.005, -41.53972527)
]

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

