# Example 4.A.10
# Butterworth bandstop (order = 8)
# Bandstop filter format

F = 600	# samples/second
fp1 = 60.00	# Hz
fp2 = 240.00	# Hz
fs1 = 120.00	# Hz
fs2 = 180.00	# Hz
ripple_passband = 0.50	# dB
ripple_stopband = 35.00		# dB

# s-plane zeros (lowpass)
# (real, imaginary)
s_plane_zeros_lp = [
	(0.0000000, 0.0000000),
	(0.0000000, 0.0000000)
]

# s-plane poles (lowpass)
# (real, imaginary)
s_plane_poles_lp = [
	(-0.3826835, 0.9238796),
	(-0.9238796, 0.3826833)
]

# s-plane zeros (bandstop)
# (real, imaginary)
s_plane_zeros = [
	(0.0000000, 1.0000002),
	(0.0000000, 1.0000002),
	(0.0000000, 1.0000002),
	(0.0000000, 1.0000002)
]

# s-plane poles (bandstop)
# (real, imaginary)
s_plane_poles = [
	(-0.6940045, 2.3470006),
	(-1.5300284, 1.1214997),	
	(-0.1158595, -0.3918164),
	(-0.4251559, -0.3116362)
]

# z-plane zeros (bandstop)
# (real, imaginary)
z_plane_zeros = [
	(-0.0000002, 1.0000000),
	(-0.0000002, -1.0000000),
	(-0.0000002, 1.0000000),
    (-0.0000002, -1.0000000),
	(-0.0000002, 1.0000000),
	(-0.0000002, -1.0000000),
	(-0.0000002, 1.0000000),
	(-0.0000002, -1.0000000)
]

# z-plane poles (bandstop)
# (real, imaginary)
z_plane_poles = [
	(-0.5956095, 0.5602728),
	(-0.5956095, -0.5602728),
	(-0.3393151, 0.2928655)	
	(-0.3393151, -0.2928655),
	(0.5956093, 0.5602730),
	(0.5956093, -0.5602730),
	(0.3393149, 0.2928655),
	(0.3393149, -0.2928655)
]

# Second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2,
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, 0.0000005, 1.0000000, 1.1912190, 0.6686563],
	[2, 0.0000005, 1.0000000, 0.6786303, 0.2009049],
	[3, 0.0000005, 1.0000000, -1.1912186, 0.6686563],
	[4, 0.0000005, 1.0000000, -0.6786298, 0.2009048]
]

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.08377],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.15031],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.35345],
	["STAGE 3 NORMALIZING FACTOR", "C3", 1.55668],
	["STAGE 4 NORMALIZING FACTOR", "C4", 1.01293]
]

# frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.000, -0.000],
	[5.000, 0.000],
	[10.000, -0.000],
	[15.000, -0.000],
	[20.000, -0.000],
	[25.000, -0.000],
	[30.000, -0.001],
	[35.000, -0.003],
	[40.000, -0.011],
	[45.000, -0.031],
	[50.000, -0.083],
	[55.000, -0.211],
	[60.000, -0.500],
	[67.200, -1.532],
	[74.400, -3.840],
	[81.600, -7.609],
	[88.800, -12.405],
	[96.000, -17.834],
	[103.200, -23.811],
	[110.400, -30.474],
	[117.600, -38.148],
	[124.800, -47.429],
	[132.000, -59.520],
	[139.200, -77.299],
	[146.400, -89.989],
	[153.600, -89.989],
	[160.800, -77.299],
	[168.000, -59.520],
	[175.200, -47.429],
	[182.400, -38.148],
	[189.600, -30.474],
	[196.800, -23.811],
	[204.000, -17.834],	
	[211.200, -12.405],
	[218.400, -7.609],
	[225.600, -3.840],
	[232.800, -1.531],
	[240.000, -0.500],
	[244.615, -0.226],
	[249.231, -0.097],
	[253.846, -0.039],
	[258.462, -0.015],
	[263.077, -0.005],
	[267.692, -0.002],
	[272.308, -0.000],
	[276.923, -0.000],
	[281.538, -0.000],
	[286.154, -0.000],
	[290.769, -0.000],
	[295.385, -0.000]
]

ex_4_a_3_constants = {
    "fp1": fp1,
	"fp2": fp2,
	"Ap": ripple_passband,
	"fs1": fs1,
	"fs2": fs2,
	"As": ripple_stopband,
	"F": F,
	"s_plane_zeros_lp": s_plane_zeros_lp,
	"s_plane_poles_lp": s_plane_poles_lp,
	"s_plane_zeros": s_plane_zeros,
	"s_plane_poles": s_plane_poles,
	"z_plane_zeros": z_plane_zeros,
	"z_plane_poles": z_plane_poles,
	"section_coefficients": section_coefficients,
	"normalizing_factors": normalizing_factors,
	"frequency_response": frequency_response
}
