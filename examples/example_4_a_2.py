
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

