from .examples_3_1_1_iir import (
    compute_filter_order,
    lowpass_computations,
    FilterType,
    FilterFamily,
    butterworth_analog_poles,
    butterworth_digital_poles,
    frequency_scaling_parameter,
    iir_filter
    )
from signal_processor.utility import polynomial_coefficients
import numpy as np

# Example 4.A.1
# Butterworth lowpass (order = 10)
# Lowpass filter format

F = 2500	# samples/second
fp1 = 0.00	# Hz
fp2 = 500.00	# Hz
fs1 = 0.00	# Hz
fs2 = 750	# Hz
ripple_passband = 0.1737	# dB
ripple_stopband = 40.00		# dB

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

maximum_passband_attenuation = ripple_passband
minimum_stopband_attenuation = ripple_stopband
passband_edge_frequency = fp2
stopband_edge_frequency = fs2
sampling_frequency = F

K, A = lowpass_computations(maximum_passband_attenuation,
	minimum_stopband_attenuation,
	passband_edge_frequency,
	stopband_edge_frequency,
	sampling_frequency)

parameter_K = K
parameter_A = A
filter_family = FilterFamily.BUTTERWORTH

N = compute_filter_order(parameter_K, parameter_A, filter_family)
N = 10
analog_poles = butterworth_analog_poles(N)
Ap = maximum_passband_attenuation
alpha = frequency_scaling_parameter(FilterFamily.BUTTERWORTH, fp2, F, N=N, Ap=Ap)
print(alpha)
digital_poles = butterworth_digital_poles(analog_poles, alpha)
results = analog_poles
print("-------------")
print("s-plane poles")
print("-------------")
for pole in s_plane_poles:
    print(pole)
print("------------------------")
print("Calculated s-plane poles")
print("------------------------")
for result in results:
    print(result)
results = digital_poles
print("-------------")
print("Digital poles")
print("-------------")
for pole in z_plane_poles:
    print(pole)
print("------------------------")
print("Calculated digital poles")
print("------------------------")
for result in results:
    print(result)
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

# Plot result
import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, x, label="Input")
plt.plot(t, y, label="Filtered")
plt.xlabel("Time (s)")
plt.legend()
plt.show()


