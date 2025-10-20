from signal_processor.infinite_impulse_response import compute_filter_order, lowpass_computations, FilterType, FilterFamily
from signal_processor.infinite_impulse_response import butterworth_analog_poles

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
N = 2 * len(s_plane_poles)
results = butterworth_analog_poles(N)
