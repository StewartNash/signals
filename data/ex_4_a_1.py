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

# second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, 2.0000000, 1.0000000, -0.2740197, 0.7324039],
	[2, 2.0000000, 1.0000000, -0.2184297, 0.3809528],
	[3, 2.0000000, 1.0000000, -0.1862828, 0.1777139],
	[4, 2.0000000, 1.0000000, -0.1682881, 0.0639486],
	[5, 2.0000000, 1.0000000, -0.1601547, 0.0125276]
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
	[0.000, -0.000],
	[20.000, -0.000],
	[40.000, -0.000],
	[60.000, -0.000],
	[80.000, -0.000],
	[100.000, -0.000],
	[120.000, -0.000],
	[140.000, -0.000],
	[160.000, -0.000],
	[180.000, -0.000],
	[200.000, -0.000],
	[220.000, -0.000],
	[240.000, -0.000],
	[260.000, -0.000],
	[280.000, -0.000],
	[300.000, -0.000],
	[320.000, -0.000],
	[340.000, -0.000],
	[360.000, -0.000],
	[380.000, -0.000],
	[400.000, -0.001],
	[420.000, -0.002],
	[440.000, -0.007],
	[460.000, -0.021],
	[480.000, -0.061],
	[500.000, -0.174],
	[530.000, -0.776],
	[560.000, -2.816],
	[590.000, -7.138],
	[620.000, -12.988],
	[650.000, -19.367],
	[680.000, -25.911],
	[710.000, -32.556],
	[740.000, -39.317],
	[770.000, -46.233],
	[800.000, -53.352],
	[830.000, -60.724],
	[860.000, -68.398],
	[890.000, -76.336],
	[920.000, -83.899],
	[950.000, -88.637],
	[980.000, -89.842],
	[1010.000, -89.987],
	[1040.000, -89.999],
	[1070.000, -90.000],
	[1100.000, -90.000],
	[1130.000, -90.000],
	[1160.000, -90.000],
	[1190.000, -90.000],
	[1220.000, -90.000]
]

ex_4_a_1_constants = {
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
