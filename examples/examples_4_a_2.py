from signals.infinite_impulse_response import (
    compute_filter_order,
    hplp_parameters,
    lowpass_parameters,
    chebyshev_analog_poles,
    chebyshev_digital_poles,
    frequency_scaling_parameter,
    iir_filter
    )
from signals.filter import FilterType, FilterFamily
from signals.utility import polynomial_coefficients
import numpy as np
from plotting.plotting import plot_digital_response

# ----------------------------------
# Example 4.A.2
#
# Chebyshev Lowpass
# (Order = 6)
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

# s-plane zeros (lowpass)
# (real, imaginary)
s_plane_zeros = [
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000)
]

# s-plane poles (lowpass)
# (real, imaginary)
s_plane_poles = [
	(-0.1017847, 1.0379357),
	(-0.1017847, -1.0379357),	
	(-0.2780809, 0.7598216),
	(-0.2780809, -0.7598216),
	(-0.3798656, 0.2781140),
	(-0.3798656, -0.2781140)
]

# z-plane zeros (lowpass)
# (real, imaginary)
z_plane_zeros = [
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000),
	(-1.0000000, 0.0000000)
]

# z-plane poles (lowpass)
# (real, imaginary)
z_plane_poles = [
	(0.2472978, 0.8758249),
	(0.2472978, -0.8758249),	
	(0.3740355, 0.6310338),
	(0.3740355, -0.6310338),
	(0.5290679, 0.2421385),
	(0.5290679, -0.2421385)
]

# Second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2,
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, 2.0000000, 1.0000000, -0.4945955, 0.8282254],
	[2, 2.0000000, 1.0000000, -0.7480710, 0.5381062],
	[3, 2.0000000, 1.0000000, -1.0581359, 0.3385440]
]

filter_family = FilterFamily.CHEBYSHEV
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
K, A, parameter_epsilon, parameter_lambda = hplp_parameters(maximum_passband_attenuation,
	minimum_stopband_attenuation,
	passband_edge_frequency,
	stopband_edge_frequency,
	sampling_frequency)	
parameter_K = K
parameter_A = A
N = compute_filter_order(parameter_K, parameter_A, filter_family)
print("K, A, N:", K, A, N)

alpha = frequency_scaling_parameter(FilterFamily.CHEBYSHEV,
        sampling_frequency,
        passband_frequency,
        order=N,
        passband_ripple=Ap,
        stopband_frequency=stopband_frequency,
        filter_type=FilterType.LOWPASS)
print("alpha: ", alpha)
analog_poles = chebyshev_analog_poles(N, parameter_epsilon)
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
digital_poles = chebyshev_digital_poles(N, parameter_epsilon, frequency_scaling=alpha)
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

plot_digital_response(digital_poles, z_plane_zeros, sampling_frequency)

