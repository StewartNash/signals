import math

# Fig. 6.27, p. 282
#########################################
# BIT REVERSE SUBROUTINE		#
# NLOG2 = NUMBER OF BITS FOR B		#
# B = INPUT NUMBER TO BE BIT REVERSED	#
#########################################
def bit_reverse_sub(B, NLOG2):
	B1 = B
	BR = 0
	for i in range(NLOG2):
		B2 = B1 / 2
		BR = BR * 2 + (B1 - 2 * B2)
		B1 = B2
	return B2
	
# Fig. 6.27, p. 282
#################################
# Bit Reverse Data Vector	#
# N = FFT LENGTH		#
# XR = REAL INPUT VECTOR	#
# XI = IMAGINARY INPUT VECTOR	#
#################################
def bit_reverse(N):
	XR = [0] * 1024
	XI = [0] * 1024
	print("BIT REVERSAL FOR DATA VECTOR IN PROGRESS")
	NLOG2 = math.log10(N) / math.log10(2)
	for j in range(N - 1 + 1):
		BR = bit_reverse_sub(j, NLOG2)
		print(f"BIT REVERSAL FOR j = {j}, BR = {BR}")
		K = BR
		if K <= j:
			continue
		REAL = XR(j)
		IMAG = X1(j)
		XR(j) = XR(K)
		XI(j) = XI(K)
		XR(K) = REAL
		XI(K) = IMAG
	return XR, XI 
