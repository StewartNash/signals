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

# s-plane zeros (real, imaginary)
s_plane_zeros = [
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000)
]

# s-plane poles (real, imaginary)
s_plane_poles = [
	(-0.1564345, 0.9876885),
	(-0.4539906, 0.8910065),
	(-0.7071068, 0.7071067),
	(-0.8910066, 0.4539905),
	(-0.9876884, 0.1564344)
]

# z-plane zeros (real, imaginary)
z_plane_zeros = [
	(1.0000000, 0.0000000),
	(1.0000000, 0.0000000),
	(1.0000000, 0.0000000),
	(1.0000000, 0.0000000),
	(1.0000000, 0.0000000)
]

# z-plane poles (real, imaginary)
z_plane_poles = [
	(0.1370101, 0.8447676),
	(0.1092151, 0.6074742),
	(0.0931416, 0.4111430),
	(-0.0841442, 0.2384709),
	(-0.0800775, 0.0782001)
]

# second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, -2.0000000, 1.0000000, 0.2740203, 0.7324040],
	[2, -2.0000000, 1.0000000, 0.2184302, 0.3809528],
	[3, -2.0000000, 1.0000000, 0.1862832, 0.1777139],
	[4, -2.0000000, 1.0000000, 0.1682884, 0.0639486],
	[5, -2.0000000, 1.0000000, 0.1601550, 0.0125277]
]

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.00125],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.11360],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.25799],
	["STAGE 3 NORMALIZING FACTOR", "C3", 0.32522],
	["STAGE 4 NORMALIZING FACTOR", "C4", 0.36908],
	["STAGE 5 NORMALIZING FACTOR", "C5", 0.35624]
]

# Frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.000, -90.000],
	[30.000, -90.000],
	[60.000, -90.000],
	[90.000, -90.000],
	[120.000, -90.000],
	[150.000, -90.000],
	[180.000, -90.000],
	[210.000, -89.999],
	[240.000, -89.987],
	[270.000, -89.842],
	[300.000, -88.637],
	[330.000, -83.899],
	[360.000, -76.336],
	[390.000, -68.398],
	[420.000, -60.724],
	[450.000, -53.352],
	[480.000, -46.233],
	[510.000, -39.317],
	[540.000, -32.556],
	[570.000, -25.911],
	[600.000, -19.367],
	[630.000, -12.988],
	[660.000, -7.138],
	[690.000, -2.816],
	[720.000, -0.776],
	[750.000, -0.174],
	[770.000, -0.061],
	[790.000, -0.021],
	[810.000, -0.007],
	[830.000, -0.002],
	[850.000, -0.001],
	[870.000, -0.000],
	[890.000, -0.000],
	[910.000, -0.000],
	[930.000, -0.000],
	[950.000, -0.000],
	[970.000, -0.000],
	[990.000, -0.000],
	[1010.000, -0.000],
	[1030.000, -0.000],
	[1050.000, -0.000],
	[1070.000, -0.000],
	[1090.000, -0.000],
	[1110.000, -0.000],
	[1130.000, -0.000],
	[1150.000, -0.000],
	[1170.000, -0.000],
	[1190.000, -0.000],
	[1220.000, 0.000]
]

ex_4_a_4_constants = {
    "fp1": fp1,
	"fp2": fp2,
	"Ap": ripple_passband,
	"fs1": fs1,
	"fs2": fs2,
	"As": ripple_stopband,
	"F": F,
	"s_plane_zeros": s_plane_zeros,
	"s_plane_poles": s_plane_poles,
	"z_plane_zeros": z_plane_zeros,
	"z_plane_poles": z_plane_poles,
	"section_coefficients": section_coefficients,
	"normalizing_factors": normalizing_factors,
	"frequency_response": frequency_response
}

