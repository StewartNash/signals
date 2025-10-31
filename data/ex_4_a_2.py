# Example 4.A.2
# Chebyshev lowpass (order = 6)
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

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.00453],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.06794],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.19751],
	["STAGE 3 NORMALIZING FACTOR", "C3", 0.33721]
]

# frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.0000, -0.173],
	[20.000, -0.166],
	[40.000, -0.145],
	[60.000, -0.115],
	[80.000, -0.079],
	[100.000, -0.044],
	[120.000, -0.016],
	[140.000, -0.001],
	[160.000, -0.003],
	[180.000, -0.022],
	[200.000, -0.055],
	[220.000, -0.096],
	[240.000, -0.136],
	[260.000, -0.164],
	[280.000, -0.173],
	[300.000, -0.157],
	[320.000, -0.117],
	[340.000, -0.064],
	[360.000, -0.017],
	[380.000, 0.000],
	[400.000, -0.031],
	[420.000, -0.103],
	[440.000, -0.167],
	[460.000, -0.147],
	[480.000, -0.023],
	[500.000, -0.173],
	[530.000, -3.574],
	[560.000, -10.327],
	[590.000, -17.009],
	[620.000, -23.055],
	[650.000, -28.616],
	[680.000, -33.856],
	[710.000, -38.889],	
	[740.000, -43.802],
	[770.000, -48.664],
	[800.000, -53.535],
	[830.000, -58.468],
	[860.000, -63.515],
	[890.000, -68.723],
	[920.000, -74.118],
	[950.000, -79.615],
	[980.000, -84.726],
	[1010.000, -88.247],
	[1040.000, -89.633],
	[1070.000, -89.946],
	[1100.000, -89.994],
	[1130.000, -90.000],
	[1160.000, -90.000],
	[1190.000, -90.000],
	[1220.000, -90.000]
]

ex_4_a_2_constants = {
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

