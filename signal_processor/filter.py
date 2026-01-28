import enum
import math
import numpy as np
import matplotlib.pyplot as plt

# IIR Filter Design Procedure
# 1. Enter filter specifications
#	a. Filter type: LP, HP, BP or BS
#	b. Filter parameters
#		i. LP, HP: Ap, As, fp, fs, F
#			A. LP: (fp < fs), (F > 2*fs)
#			B. HP: (fp > fs), (F > 2*fp)
#		ii. BP, BS: Ap, As, fp1, fp2, fs1, fs2, F/2
#			A. BP: (fs1 < fp1 < fp2 < fs2), (F > 2*fs2)
#			B. BS: (fp1 < fs1 < fs2 < fp2), (F > 2*fp2) 
# 2. Compute filter order, N (table 4.4)
# 3. Compute analog LP zeros
# 4. Compute analog LP poles
# 5. Compute digital poles and zeros
# 6. Compute second order section coefficients
# 7. Format coefficients as a function of section index, k
# 8. Compute coefficients B1,k for odd first-order section (N-odd only)
# 9. Determine second order section normalization coefficients

#TODO: Create a Filter class which encapsulates all filter parameters

# filter_order			nk, NK
# passband_frequency		fp
# passband_frequency_low	fp1, FP1
# passband_frequency_high	fp2, FP2
# stopband_frequency		fs, FS, f, F
# sampling_frequency		fs, FS, f, F (CORRECTION)
# stopband_frequency_low	fs1, fa1, FA1
# stopband_frequency_high	fs2, fa2, FA2
# transition_bandwidth_low	bt1
# transition_bandwidth_high	bt2
# transition_bandwidth		bt
# delta				_del
# delta_passband (ripple)	d1
# delta_stopband (ripple)	d2
# actual_passband_ripple	aap
# specified_passband_ripple	ap
# actual_stopband_attenuation	actual_minimum_stopband_attenuation
# minimum_stopband_attenuation	specified_minimum_stopband_attenuation
# minimum_stopband_attenuation	aa
# parameter_d			pard
# alpha				alp, ALP

# actual_passband_ripple	aa (CORRECTION)
# minimum_stopband_attenuation	aap (CORRECTION)
# kaiser_coeffs			wk, WK
# mod_bessel_fk_alpha		modified_bessel_first_kind_alpha
# mod_bessel_fk_beta		modified_bessel_first_kind_beta
# mod_bessel_fk_alpha		IOALP
# mod_bessel_fk_beta		IOBE
# beta				BE
#				KFAC (factorial)
# cutoff_frequency		wc, WC
# cutoff_frequency_low		wc1, WC1
# cutoff_frequency_high		wc2, WC2
# initial_impulse_response	H1
# impulse_response		H
# sinc_function			fnsx, FNSX
# argument			ARG

# LOWPASS			LP
# HIGHPASS			HP
# BANDPASS			BP
# BANDSTOP			BS
# maximum_passband_attenuation	Ap	[positive dB]
# minimum_stopband_attenuation	As	[positive dB]
# passband_edge_frequency	fp
# stopband_edge_frequency	fs
# transition_bandwidth		fp <= f <= fs
# sampling_rate			F
# nyquist_frequency		F/2


class FilterFamily(enum.Enum):
	BESSEL = 1
	BUTTERWORTH = 2
	CHEBYSHEV = 3
	ELLIPTIC = 4	
	CHEBYSHEV_1 = 5
	CHEBYSHEV_2 = 6


class FilterType(enum.Enum):
	LOWPASS = 1
	HIGHPASS = 2
	BANDPASS = 3
	BANDSTOP = 4


class FilterWindow(enum.Enum):
    NONE = 0
    TRIANGULAR = 1 # p. 264
    HANN = 2 # (HANNING) p. 267
    RECTANGULAR = 1 # p. 205
    HAMMING = 2 # pp. 206, 269
    BLACKMAN = 3 # (BLACKMAN_HARRIS) pp. 206, 270
    KAISER = 4 #   (KAISER_BESSEL) pp. 207, 271


class Filter:
	def __init__(self):
		self.family = None
		self.type = None
		self.passband_frequency_low = None
		self.passband_frequency_high = None
		self.stopband_frequency_low = None
		self.stopband_frequency_high = None
		self.sampling_frequency = None
		self.specified_passband_ripple = None
		self.actual_passband_ripple = None
		self.minimum_stopband_attenuation = None
		self.stopband_attenuation = None

		self.order = None
		self.coefficients = None
		self.index = None
		self.buffer = None
		
	def create_filter(self,
		filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		sampling_frequency,
		specified_passband_ripple,
		minimum_stopband_attenuation):
		pass
		
	def get_analog_poles(self):
		pass
		
	def get_digital_poles(self):
		pass
	
	def get_parameters(self):
		pass
		
	def get_parameter_descriptions(self):
		pass
		
	def set_parameters(self, filter_parameters):
	    if "type" in filter_parameters:
	        self.type = filter_parameters["type"]
	    if "family" in filter_parameters:
	        self.family = filter_parameters["family"]
	    if "stopband_attenuation" in filter_parameters:
	        self.stopband_attenuation = filter_parameters["stopband attenuation"]
	    if "passband_attenuation" in filter_parameters:
	        self.specified_passband_ripple = filter_parameters["passband attenuation"]
	    if self.type is FilterType.LOWPASS:
	        if "passband frequency" in filter_parameters:
	            self.passband_frequency_high = filter_parameters["passband frequency"]
	            self.passband_frequency_low = 0
	        if "stopband frequency" in filter_parameters:
	            self.stopband_frequency_low = filter_parameters["stopband frequency"]
	            self.stopband_frequency_high = float('inf')
	    
		

