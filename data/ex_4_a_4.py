# Example 4.A.4
# Butterworth highpass (order = 10)
# Highpass filter format

F = 2500	# samples/second
fp1 = 750.00	# Hz
fp2 = 0.00	# Hz
fs1 = 500.00	# Hz
fs2 = 0.00	# Hz
ripple_passband = 0.1737	# dB
ripple_stopband = 40.00		# dB

passband_frequency_low = 0 # Hz
passband_frequency_high = passband_frequency
stopband_frequency_low = stopband_frequency
stopband_frequency_high = float('inf') # Hz

