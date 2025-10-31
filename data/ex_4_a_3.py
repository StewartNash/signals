# Example 4.A.3
# Elliptic lowpass (order = 4)
# Lowpass filter format

F = 2500	# samples/second
fp1 = 0.00	# Hz
fp2 = 500.00	# Hz
fs1 = 0.00	# Hz
fs2 = 750	# Hz
ripple_passband = 0.1737	# dB
ripple_stopband = 40.00		# dB

# s-plane zeros (lowpass)
# (real, imaginary)
s_plane_zeros = [
	(0.0000000, 3.3607185),
	(0.0000000, 1.4730365)
]

# s-plane poles (lowpass)
# (real, imaginary)
s_plane_poles = [
	(-0.4304955, 0.3741359),
	(-0.1375649, 0.7839348)
]

# z-plane zeros (lowpass)
# (real, imaginary)
z_plane_zeros = [
	(-0.8373247, 0.5467058),
	(-0.8373247, -0.5467058),
	(-0.3690528, 0.9294085),
	(-0.3690528, -0.9294085)
]

# z-plane poles (lowpass)
# (real, imaginary)
z_plane_poles = [
	(0.3086023, 0.3422556),
	(0.3086023, -0.3422556),	
	(0.1920363, 0.8214731,
	(0.1920363, -0.8214731)
]

# Second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2,
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, 1.6746495, 1.0000000, -0.6172046, 0.2123743],
	[2, 0.7381057, 1.0000000, -0.3840726, 0.7116959]
]

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.07699],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.16197],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.47533]
]

# frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.0000, -0.173],
	[20.000, -0.170],
	[40.000, -0.162],
	[60.000, -0.149],
	[80.000, -0.131],
	[100.000, -0.110],
	[120.000, -0.088],
	[140.000, -0.064],
	[160.000, -0.042],
	[180.000, -0.023],
	[200.000, -0.008],
	[220.000, -0.000],
	[240.000, -0.000],
	[260.000, -0.009],
	[280.000, -0.027],
	[300.000, -0.053],
	[320.000, -0.086],
	[340.000, -0.120],
	[360.000, -0.150],
	[380.000, -0.170],
	[400.000, -0.170],
	[420.000, -0.144],
	[440.000, -0.090],
	[460.000, -0.024],
	[480.000, -0.004],
	[500.000, -0.173],
	[530.000, -1.359],
	[560.000, -4.283],
	[590.000, -8.507],
	[620.000, -13.250],
	[650.000, -18.247],
	[680.000, -23.611],
	[710.000, -29.757],	
	[740.000, -37.875],
	[770.000, -56.963],
	[800.000, -46.562],
	[830.000, -42.486],
	[860.000, -41.678],
	[890.000, -42.291],
	[920.000, -43.952],
	[950.000, -46.780],
	[980.000, -51.614],
	[1010.000, -63.875],
	[1040.000, -57.937],
	[1070.000, -50.401],
	[1100.000, -46.815],
	[1130.000, -44.638],
	[1160.000, -43.231],
	[1190.000, -42.338],
	[1220.000, -41.839]
]

ex_4_a_3_constants = {
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

