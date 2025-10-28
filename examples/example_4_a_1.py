from signal_processor.infinite_impulse_response import compute_filter_order, lowpass_computations, FilterType, FilterFamily
from signal_processor.infinite_impulse_response import butterworth_analog_poles, butterworth_digital_poles, frequency_scaling_parameter

# ----------------------------------
# Example 4.A.1: Butterworth Lowpass
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

N = 2 * len(s_plane_poles)
Ap = actual_passband_ripple
alpha = frequency_scaling_parameter(FilterFamily.CHEBYSHEV,
        sampling_frequency,
        passband_frequency,
        order=N,
        passband_ripple=Ap,
        stopband_frequency=stopband_frequency,
        filter_type=FilterType.LOWPASS)
results = butterworth_analog_poles(N)
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
results = butterworth_digital_poles(N, frequency_scaling=alpha)
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
    
