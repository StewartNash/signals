# Example 4.A.11
# Chebyshev bandstop (order = 6)
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
	(-0.3132283, 1.0219275),
	(-0.6264565, 0.0000000)
]

# s-plane zeros (bandstop)
# (real, imaginary)
s_plane_zeros = [
	(0.0000000, 1.0000002),
	(0.0000000, 1.0000002),
	(0.0000000, 1.0000002)
]

# s-plane poles (bandstop)
# (real, imaginary)
s_plane_poles = [
	(-0.6735228, 2.7999786),
	(-0.2407656, -4.1534181),	
	(-0.0812110, -0.3376109)
]

# z-plane zeros (bandstop)
# (real, imaginary)
z_plane_zeros = [
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
	(-0.6854445, 0.5262842),
	(-0.6854445, -0.5262842),
	(0.6119079, 0.6119081)	
	(0.6119079, -0.6119081),
	(0.6854441, 0.5262842),
	(0.6854441, -0.5262842)
]

# Second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2,
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, 0.0000005, 1.0000000, 1.3708891, 0.7468092],
	[2, 0.0000005, 1.0000000, 0.0000001, -0.3744314],
	[3, 0.0000005, 1.0000000, -1.3708882, 0.7468087]
]

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.09165],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.09562],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.56727],
	["STAGE 3 NORMALIZING FACTOR", "C3", 1.68955]
]

# frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.000, 0.000],
	[5.000, -0.024],
	[10.000, -0.093],
	[15.000, -0.194],
	[20.000, -0.309],
	[25.000, -0.414],
	[30.000, -0.485],
	[35.000, -0.495],
	[40.000, -0.425],
	[45.000, -0.269],
	[50.000, -0.075],
	[55.000, -0.016],
	[60.000, -0.500],
	[67.200, -3.022],
	[74.400, -7.278],
	[81.600, -12.026],
	[88.800, -16.799],
	[96.000, -21.600],
	[103.200, -26.573],
	[110.400, -31.919],
	[117.600, -37.929],
	[124.800, -45.074],
	[132.000, -54.279],
	[139.200, -67.840],
	[146.400, -89.147],
	[153.600, -89.147],
	[160.800, -67.840],
	[168.000, -54.273],
	[175.200, -45.074],
	[182.400, -37.400],
	[189.600, -31.919],
	[196.800, -26.573],
	[204.000, -21.600],	
	[211.200, -16.799],
	[218.400, -12.026],
	[225.600, -7.278],
	[232.800, -3.022],
	[240.000, -0.500],
	[244.615, -0.027],
	[249.231, -0.050],
	[253.846, -0.224],
	[258.462, -0.386],
	[263.077, -0.479],
	[267.692, -0.499],
	[272.308, -0.458],
	[276.923, -0.377],
	[281.538, -0.274],
	[286.154, -0.169],
	[290.769, -0.080],
	[295.385, -0.021]
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

