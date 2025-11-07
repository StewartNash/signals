from signal_processor.infinite_impulse_response import (
    compute_filter_order,
    lowpass_parameters,
    butterworth_analog_poles,
    butterworth_digital_poles,
    butterworth_digital_poles_alternate,
    frequency_scaling_parameter,
    iir_filter
    )
from signal_processor.filter import FilterType, FilterFamily
from signal_processor.utility import polynomial_coefficients
import numpy as np
from plotting.plotting import plot_digital_response

# ----------------------------------
# Example 4.A.1
#
# Butterworth Lowpass
# (Order = 10)
# ----------------------------------
# Infinite impulse response
# Sample rate = 2500 samples/second

FREQUENCY_RESOLUTION = 500

# Filter specifications
actual_passband_ripple = 0.1737  # dB (less than)
minimum_stopband_attenuation = 40  # dB (greater than)
passband_frequency = 500  # Hz
stopband_frequency = 750  # Hz
sampling_frequency = 2500  # Hz

passband_frequency_low = 0 # Hz
passband_frequency_high = passband_frequency
stopband_frequency_low = stopband_frequency
stopband_frequency_high = float('inf') # Hz

s_plane_poles = [
	(-0.1564345, 0.9876885),
	(-0.4539906, 0.8910065),
	(-0.7071068, 0.7071067),

(-0.8910066, 0.4539905),
	(-0.9876884, 0.1564344)
]

# z-plane zeros (real, imaginary)
z_plane_zeros = [
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000)
]

# z-plane poles (real, imaginary)
z_plane_poles = [
	(0.1370099, 0.8447676),
	(0.1092149, 0.6074742),
	(0.0931414, 0.4111430),
	(0.0841441, 0.2384710),
	(0.0800774, 0.0782001)
]

filter_family = FilterFamily.BUTTERWORTH
# Eliminate or reduce renaming from legacy code
maximum_passband_attenuation = actual_passband_ripple
passband_edge_frequency = passband_frequency
stopband_edge_frequency = stopband_frequency
Ap = actual_passband_ripple
F = sampling_frequency

K, A = lowpass_parameters(maximum_passband_attenuation,
	minimum_stopband_attenuation,
	passband_edge_frequency,
	stopband_edge_frequency,
	sampling_frequency)
parameter_K = K
parameter_A = A
N = compute_filter_order(parameter_K, parameter_A, filter_family)
print("K, A, N:", K, A, N)

alpha = frequency_scaling_parameter(FilterFamily.BUTTERWORTH,
        sampling_frequency,
        passband_frequency,
        order=N,
        passband_ripple=Ap,
        stopband_frequency=stopband_frequency,
        filter_type=FilterType.LOWPASS)
print("alpha: ", alpha)
analog_poles = butterworth_analog_poles(N)
print("-------------")
print("s-plane poles")
print("-------------")
for pole in s_plane_poles:
    print(pole)
print("------------------------")
print("Calculated s-plane poles")
print("------------------------")
for pole in analog_poles:
    print(pole)
#digital_poles = butterworth_digital_poles_alternate(analog_poles, alpha)
digital_poles = butterworth_digital_poles(N, frequency_scaling=alpha)
print("-------------")
print("Digital poles")
print("-------------")
for pole in z_plane_poles:
    print(pole)
print("------------------------")
print("Calculated digital poles")
print("------------------------")
for pole in digital_poles:
    print(pole)
denominator_coefficients = polynomial_coefficients(digital_poles)
numerator_coefficients = [(2, 1)] * len(denominator_coefficients)
print("------------------------")
print("Denominator Coefficients")
print("------------------------")
for coefficient in denominator_coefficients:
    print(coefficient)

b = numerator_coefficients
a = denominator_coefficients
fs = 1000  # Hz
t = np.arange(0, 0.1, 1 / F)
x = np.sin(2 * np.pi * 125 * t) + 0.5 * np.random.randn(len(t))  # 125 Hz sine + noise

t = t.tolist()
x = x.tolist()

# Filter the signal
y = iir_filter(x, b, a)

## Plot result
#import matplotlib.pyplot as plt
#plt.figure()
#plt.plot(t, x, label="Input")
#plt.plot(t, y, label="Filtered")
#plt.xlabel("Time (s)")
#plt.legend()
#plt.show()

plot_digital_response(digital_poles, z_plane_zeros, sampling_frequency)
