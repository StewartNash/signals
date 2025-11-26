# Example 4.A.12
# Elliptic bandstop (order = 6)
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
	(0.0000000, 2.3681457),
	(0.0000000, 0.0000000)
]

# s-plane poles (lowpass)
# (real, imaginary)
s_plane_poles_lp = [
	(-0.1477767, 0.4982435),
	(-0.3105073, 0.0000000)
]

# s-plane zeros (bandstop)
# (real, imaginary)
s_plane_zeros = [
	(0.0000000, -0.7567176),
	(0.0000000, 1.0000002),
	(0.0000000, 1.3214975)
]

# s-plane poles (bandstop)
# (real, imaginary)

#s_plane_poles = [
#	(-0.6530900, 2.8054663),
#	(-0.2462344, -4.0611711), # Two real poles from odd-order lowpass s-plane # = 2	
#	(-0.0787125, -0.3381235)
#]
s_plane_poles = [
	(-0.6530900, 2.8054663),
	(-0.2462344, -4.0611711),
	(-0.2462344, -4.0611711),
	(-0.0787125, -0.3381235)
]


# z-plane zeros (bandstop)
# (real, imaginary)
z_plane_zeros = [
	(0.2717618, 0.9623646),
	(0.2717618, -0.9623646),
	(-0.0000002, 1.0000000),
    (-0.0000002, -1.0000000),
	(-0.2717622, 0.9623645),
	(-0.2717622, -0.9623645)
]

# z-plane poles (bandstop)
# (real, imaginary)

#z_plane_poles = [
#	(-0.6881948, 0.5291661),
#	(-0.6881948, -0.5291661),
#	(0.6048345, -0.6048345), # Two real poles from odd-order lowpass s-plane # = 2	
#	(0.6881944, 0.5291662),
#	(0.6881944, -0.5291662)
#]
z_plane_poles = [
	(-0.6881948, 0.5291661),
	(-0.6881948, -0.5291661),
	(0.6048345, -0.6048345),
	(0.6048345, -0.6048345),
	(0.6881944, 0.5291662),
	(0.6881944, -0.5291662)
]

# Second-order section coefficients
# stage
# numerator coefficient A1
# numerator coefficient A2,
# denominator coefficient B1
# denominator coefficient B2
# [stage, A1, A2, B1, B2]
section_coefficients = [
	[1, -0.5435236, 1.0000000, 1.3763895, 0.7536287],
	[2, 0.0000005, 1.0000000, 0.0000001, -0.3658248],
	[3, 0.5435243, 1.0000000, -1.3763888, 0.7536284]
]

# Normalizing factors
# [Name, Designation, Value]
normalizing_factors = [
	["IIR NORMALIZING FACTOR", "C0", 0.10107],
	["STAGE 1 NORMALIZING FACTOR", "C1", 0.06980],
	["STAGE 2 NORMALIZING FACTOR", "C2", 0.57609],
	["STAGE 3 NORMALIZING FACTOR", "C3", 2.51345]
]

# frequency response output
# [frequency, magnitude]
frequency_response = [
	[0.000, 0.000],
	[5.000, -0.024],
	[10.000, -0.091],
	[15.000, -0.190],
	[20.000, -0.303],
	[25.000, -0.409],
	[30.000, -0.482],
	[35.000, -0.497],
	[40.000, -0.432],
	[45.000, -0.280],
	[50.000, -0.082],
	[55.000, -0.013],
	[60.000, -0.500],
	[67.200, -3.151],
	[74.400, -7.668],
	[81.600, -12.736],
	[88.800, -17.918],
	[96.000, -23.310],
	[103.200, -29.230],
	[110.400, -36.331],
	[117.600, -46.617],
	[124.800, -65.567],
	[132.000, -52.566],
	[139.200, -53.391],
	[146.400, -61.624],
	[153.600, -61.624],
	[160.800, -53.391],
	[168.000, -52.566],
	[175.200, -65.567],
	[182.400, -46.617],
	[189.600, -36.331],
	[196.800, -29.230],
	[204.000, -23.310],	
	[211.200, -17.918],
	[218.400, -12.736],
	[225.600, -7.668],
	[232.800, -3.151],
	[240.000, -0.500],
	[244.615, -0.024],
	[249.231, -0.056],
	[253.846, -0.235],
	[258.462, -0.394],
	[263.077, -0.482],
	[267.692, -0.498],
	[272.308, -0.454],
	[276.923, -0.371],
	[281.538, -0.268],
	[286.154, -0.165],
	[290.769, -0.078],
	[295.385, -0.020]
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

