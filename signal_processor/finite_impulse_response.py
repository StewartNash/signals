import math
import numpy as np
from signal_processor.filter import FilterType, FilterFamily, Filter

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

def kaiser_coefficients(filter_order, minimum_stopband_attenuation):
	n = filter_order
	if minimum_stopband_attenuation <= 21.0:
		alpha = 0
	elif minimum_stopband_attenuation <= 50.0:
		alpha = 0.5842 * (minimum_stopband_attenuation - 21) ** 0.4 + 0.07886 * (minimum_stopband_attenuation - 21)
	else:
		alpha = 0.1102 * (minimum_stopband_attenuation - 8.7)
	
	kaiser_coeffs = [0.0] * n
	for i in range(n):
		beta = alpha * math.sqrt(1 - (2 * i / (n - 1) - 1) ** 2)
		kaiser_coeffs[i] = zo_mod_bessel_fk(beta, 31) / zo_mod_bessel_fk(alpha, 31)

	return (kaiser_coeffs, alpha)

def zo_mod_bessel_fk(x, N=25):
	output = 0
	for i in range(N + 1):
		output += ((x / 2) ** i / math.factorial(i)) ** 2
		
	return output

def kaiser_filter_order(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	specified_passband_ripple,
	minimum_stopband_attenuation):

	transition_bandwidth_low  = abs(passband_frequency_high - stopband_frequency_high)
	transition_bandwidth_high = abs(passband_frequency_low - stopband_frequency_low)

	if filter_type == FilterType.LOWPASS:
		transition_bandwidth = transition_bandwidth_low
	elif filter_type == FilterType.HIGHPASS:
		transition_bandwidth = transition_bandwidth_high
	elif filter_type in (FilterType.BANDPASS, FilterType.BANDSTOP):
		transition_bandwidth = min(transition_bandwidth_low, transition_bandwidth_high)
	else:
		raise ValueError("Unsupported filter type")

	delta_stopband = 10 ** (-0.05 * minimum_stopband_attenuation)
	delta_passband = (10 ** (0.05 * specified_passband_ripple) - 1) / (10 ** (0.05 * specified_passband_ripple) + 1)
	delta = min(delta_passband, delta_stopband)
	minimum_stopband_attenuation = -20 * math.log10(delta)

	if minimum_stopband_attenuation <= 21:
		parameter_d = 0.9222
	else:
		parameter_d = (minimum_stopband_attenuation - 7.95) / 14.36
		
	filter_order = int(2 + parameter_d * sampling_frequency / transition_bandwidth)
	if filter_order % 2 == 0:
		filter_order += 1  # Make it odd

	return (filter_order, delta, minimum_stopband_attenuation, parameter_d)

def kaiser_lowpass(passband_frequency_high,
				   stopband_frequency_low,
				   sampling_frequency,
				   filter_order,
				   kaiser_coeffs):

	cutoff_frequency = 0.5 * (passband_frequency_high + stopband_frequency_low)
	impulse_response = []
	M = filter_order - 1

	for i in range(filter_order):
		k = i - M/2
		if k == 0:
			h = 2 * cutoff_frequency / sampling_frequency
		else:
			h = math.sin(2 * math.pi * cutoff_frequency * k / sampling_frequency) / (math.pi * k)
		impulse_response.append(h * kaiser_coeffs[i])

	# Normalize for unity gain at DC
	gain = sum(impulse_response)
	impulse_response = [x / gain for x in impulse_response]
	
	return impulse_response

def kaiser_highpass(passband_frequency_low,
				   stopband_frequency_high,
				   sampling_frequency,
				   filter_order,
				   kaiser_coeffs):

	cutoff_frequency = 0.5 * (passband_frequency_low + stopband_frequency_high)
	
	fp = passband_frequency_low
	fc = cutoff_frequency
	f = sampling_frequency
	impulse_response = []
	M = filter_order - 1

	omega = 2 * math.pi * (f / 2) / f
	gain = 0
	for i in range(filter_order):
		k = i - M/2
		if k == 0:
			h = 1 - 2 * fc / f
		else:
			h = - (2 * fc / f) * math.sin(2 * math.pi * k * fc / f) / (2 * math.pi * k * fc / f)
		temporary = h * kaiser_coeffs[i]
		gain += temporary * np.exp(-1j * omega * i)
		impulse_response.append(temporary)

	# Normalize for unity gain at passband frequency
	impulse_response = [x / abs(gain) for x in impulse_response]
	
	return impulse_response

def kaiser_bandpass(passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	filter_order,
	kaiser_coeffs):

	f = sampling_frequency
	fp1 = passband_frequency_low
	fp2 = passband_frequency_high
	fs1 = stopband_frequency_low
	fs2 = stopband_frequency_high

	delta_f_1 = fp1 -fs1
	delta_f_h = fs2 - fp2
	delta_f = min(delta_f_1, delta_f_h)
	cutoff_frequency_low = fp1 - delta_f / 2
	cutoff_frequency_high = fp2 + delta_f / 2

	fc1 = cutoff_frequency_low
	fc2 = cutoff_frequency_high
		
	center_frequency = (fp1 + fp2) / 2
	omega = 2 * math.pi * center_frequency / f
		
	gain = 0
	impulse_response = []
	n = filter_order - 1
	for i in range(filter_order):
		m = i - n / 2
		if m == 0:
			h = 2 * (fc2 - fc1) / f 
		else:
			h = (math.sin(2 * math.pi * m * fc2 / f) - math.sin(2 * math.pi * m * fc1 / f)) / (m * math.pi)
		temporary = h * kaiser_coeffs[i]
		gain += temporary * np.exp(1j * omega * i)
		impulse_response.append(temporary)
	
	impulse_response = [x / abs(gain) for x in impulse_response]
	
	return impulse_response
	
def kaiser_bandstop(passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	sampling_frequency,
	filter_order,
	kaiser_coeffs):

	f = sampling_frequency
	fp1 = passband_frequency_low
	fp2 = passband_frequency_high
	fs1 = stopband_frequency_low
	fs2 = stopband_frequency_high

	delta_f_1 = fs1 -fp1
	delta_f_h = fp2 - fs2
	delta_f = min(delta_f_1, delta_f_h)
	cutoff_frequency_low = fp1 + delta_f / 2
	cutoff_frequency_high = fp2 - delta_f / 2

	fc1 = cutoff_frequency_low
	fc2 = cutoff_frequency_high
		
	center_frequency = (fp1 + fp2) / 2
	omega = 2 * math.pi * ((fp2 + f / 2) / 2) / f
		
	gain = 0
	impulse_response = []
	n = filter_order - 1
	for i in range(filter_order):
		m = i - n / 2
		if m == 0:
			h = 2 * (fc1 - fc2) / f + 1
		else:
			h = (math.sin(2 * math.pi * m * fc1 / f) - math.sin(2 * math.pi * m * fc2 / f)) / (m * math.pi)
		temporary = h * kaiser_coeffs[i]
		gain += temporary * np.exp(1j * omega * i)
		impulse_response.append(temporary)
	
	impulse_response = [x / abs(gain) for x in impulse_response]
	
	return impulse_response	
	
def magnitude_response(omega, impulse_response, sampling_frequency, filter_order):
	frequency = omega / (2 * math.pi)
	period = 1 / sampling_frequency
	response_magnitude = 0.0
	#real_component = 0.0
	#imaginary_component = 0.0
	for i in range(len(impulse_response)):
		response_magnitude += impulse_response[i] * np.exp(-1j * 2 * math.pi * frequency * i * period)
		#arg = 2 * math.pi * frequency * i * period
		#real_component += impulse_response[i] * math.cos(arg)
		#imaginary_component -= impulse_response[i] * math.sin(arg)
	#response_magnitude = math.sqrt(real_component ** 2 + imaginary_component ** 2)
	response_magnitude = abs(response_magnitude)
	
	return response_magnitude 

class FIRFilter(Filter):
	def __init__(self):
		super().__init__()
		
	def create_filter(self,
		filter_family,
		filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		sampling_frequency,
		specified_passband_ripple,
		minimum_stopband_attenuation):

		self.family = filter_family
		self.type = filter_type
		self.sampling_frequency = sampling_frequency
		self.passband_frequency_low = passband_frequency_low
		self.passband_frequency_high = passband_frequency_high
		self.stopband_frequency_low = stopband_frequency_low
		self.stopband_frequency_high = stopband_frequency_high
		self.specified_passband_ripple = specified_passband_ripple
		self.minimum_stopband_attenuation = minimum_stopband_attenuation 

		filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(
			filter_type=self.type,
			passband_frequency_low=self.passband_frequency_low,
			passband_frequency_high=self.passband_frequency_high,
			stopband_frequency_low=self.stopband_frequency_low,
			stopband_frequency_high=self.stopband_frequency_high,
			sampling_frequency=self.sampling_frequency,
			specified_passband_ripple=self.specified_passband_ripple,
			minimum_stopband_attenuation=self.minimum_stopband_attenuation)
		self.order = filter_order
		self.stopband_attenuation = minimum_stopband_attenuation
		
		kaiser_coeffs, alpha = kaiser_coefficients(self.order, self.stopband_attenuation)
		impulse_response = kaiser_lowpass(self.passband_frequency_high,
			self.stopband_frequency_low,
			self.sampling_frequency,
			self.order,
			kaiser_coeffs)
			
		self.coefficients = impulse_response
		self.index = 0
		self.buffer = [0.0] * len(self.coefficients)
		
	def process(self, sample):
		self.buffer[self.index] = sample
		h = self.coefficients

		N = len(h)
		# FIR convolution
		y = 0.0
		j = self.index
		for k in range(N):
			y += h[k] * self.buffer[j]
			j = (j - 1) % N

		# Advance circular index
		self.index = (self.index + 1) % N

		return y
