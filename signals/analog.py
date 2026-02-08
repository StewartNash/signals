import math
from abc import ABC, abstractmethod

from signals.filter import FilterType, FilterWindow, Filter, FilterFamily
from signals.utility import chebyshev

def butterworth_filter_coefficients(filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		specified_passband_ripple,
		minimum_stopband_attenuation):

	maximum_passband_attenuation = specified_passband_ripple
	a_p = maximum_passband_attenuation
	a_s = minimum_stopband_attenuation
	parameter_epsilon = (10 ** (0.1 * a_p) - 1) ** 0.5
	parameter_lambda = (10 ** (0.1 * a_s) - 1) ** 0.5
	parameter_a = parameter_lambda / parameter_epsilon
	
	passband_frequency = passband_frequency_high
	stopband_frequency = stopband_frequency_low
	omega_p = passband_frequency
	omega_s = stopband_frequency
	
	parameter_k0 = omega_p / omega_s
	
	filter_order = int(math.log10(parameter_a) / math.log10(1 / parameter_k0))
	
	return (filter_order, parameter_epsilon)	

def butterworth_filter_order(filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		specified_passband_ripple,
		minimum_stopband_attenuation):

	filter_order, parameter_epsilon = butterworth_filter_coefficients(
		filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		specified_passband_ripple,
		minimum_stopband_attenuation
	)
	
	return filter_order

def chebyshev_filter_coefficients(filter_type,
		passband_frequency_low,
		passband_frequency_high,
		stopband_frequency_low,
		stopband_frequency_high,
		specified_passband_ripple,
		minimum_stopband_attenuation):
	maximum_passband_attenuation = specified_passband_ripple
	a_p = maximum_passband_attenuation
	a_s = minimum_stopband_attenuation
	parameter_epsilon = (10 ** (0.1 * a_p) - 1) ** 0.5
	parameter_lambda = (10 ** (0.1 * a_s) - 1) ** 0.5
	parameter_a = parameter_lambda / parameter_epsilon

	passband_frequency = passband_frequency_high
	stopband_frequency = stopband_frequency_low
	omega_p = passband_frequency
	omega_s = stopband_frequency

	parameter_k0 = omega_p / omega_s

	filter_order = int(math.acosh(parameter_a) / math.acosh(1 / parameter_k0))

	return (filter_order, parameter_epsilon)


class AnalogFilter(Filter, ABC):
	def __init__(self):
		super().__init__()

	@abstractmethod
	def magnitude_response(self, frequencies, is_db=False):
		#frequencies = []
		magnitudes = []
		if self.family is FilterFamily.BUTTERWORTH:
			filter_order, parameter_epsilon = butterworth_filter_coefficients(
				self.type,
				self.passband_frequency_low,
				self.passband_frequency_high,
				self.stopband_frequency_low,
				self.stopband_frequency_high,
				self.specified_passband_ripple,
				self.minimum_stopband_attenuation
			)
			omega_p = 2 * math.pi * self.passband_frequency_high
			natural_frequencies = [2 * math.pi * frequency for frequency in frequencies]
			magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order))) for omega in natural_frequencies]
			if is_db:
				magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)


class ButterworthFilter(AnalogFilter):
	def __init__(self):
		super().__init__()

	def magnitude_response(self, frequencies, is_db=False):
		#frequencies = []
		#magnitudes = []
		filter_order, parameter_epsilon = butterworth_filter_coefficients(
			self.type,
			self.passband_frequency_low,
			self.passband_frequency_high,
			self.stopband_frequency_low,
			self.stopband_frequency_high,
			self.specified_passband_ripple,
			self.minimum_stopband_attenuation
		)
		omega_p = 2 * math.pi * self.passband_frequency_high
		natural_frequencies = [2 * math.pi * frequency for frequency in frequencies]
		magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order))) for omega in natural_frequencies]
		if is_db:
			magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)
		
	def get_poles(self, normalized=False):
		poles = []
		filter_order = butterworth_filter_order(
			self.type,
			self.passband_frequency_low,
			self.passband_frequency_high,
			self.stopband_frequency_low,
			self.stopband_frequency_high,
			self.specified_passband_ripple,
			self.minimum_stopband_attenuation
		)
		N = filter_order
		if N % 2 == 0:
			poles = [(-math.sin((2 * k - 1) / (2 * N) * math.pi), math.cos((2 * k - 1) / (2 * N) * math.pi)) for k in range(1, 1 + N / 2)]
			#poles = [-math.sin((2 * k - 1) / (2 * N) * math.pi) + 1j * math.cos((2 * k - 1) / (2 * N) * math.pi) for k in range(1, 1 + N / 2)]
		else:
			poles = [(-math.sin((2 * k - 1) / (2 * N) * math.pi), math.cos((2 * k - 1) / (2 * N) * math.pi)) for k in range(1, 1 + (N + 1) / 2)]
			#poles = [-math.sin((2 * k - 1) / (2 * N) * math.pi) + 1j * math.cos((2 * k - 1) / (2 * N) * math.pi) for k in range(1, 1 + (N + 1) / 2)]
		if not normalized:
			omega_p = self.passband_frequency_high
			poles  = [(s[0] * omega_p ** (- 1 / N), s[1] * omega_p ** (- 1 / N)) for s in poles]
			#poles	= [s * omega_p ** (- 1 / N) for s in poles]
			
		return poles

class ChebyshevFilter(AnalogFilter):
	def __init__(self):
		super().__init__()

	def magnitude_response(self, frequencies, is_db=False):
		# frequencies = []
		magnitudes = []
		filter_order, parameter_epsilon = chebyshev_filter_coefficients(
			self.type,
			self.passband_frequency_low,
			self.passband_frequency_high,
			self.stopband_frequency_low,
			self.stopband_frequency_high,
			self.specified_passband_ripple,
			self.minimum_stopband_attenuation
		)
		omega_p = 2 * math.pi * self.passband_frequency_high
		natural_frequencies = [2 * math.pi * frequency for frequency in frequencies]
		magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * chebyshev(omega / omega_p, filter_order) ** 2)) for
					  omega in natural_frequencies]
		if is_db:
			magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)

	def get_poles(self, normalized=False):
		poles = []
		filter_order, parameter_epsilon = chebyshev_filter_coefficients(
			self.type,
			self.passband_frequency_low,
			self.passband_frequency_high,
			self.stopband_frequency_low,
			self.stopband_frequency_high,
			self.specified_passband_ripple,
			self.minimum_stopband_attenuation
		)
		N = filter_order
		x = [(2 * k - 1) * math.pi / (2 * N) for k in range(1, 1 + N)]
		y = math.asinh(1 / parameter_epsilon) / N
		poles = [(-math.sin(x_) * math.sinh(y), math.cos(x_) * math.cosh(y)) for x_ in x]
		poles = poles + [(-math.sin(x_) * math.sinh(y), math.cos(x_) * math.cosh(y)) for x_ in x]
		#y = [math.asinh(1 / parameter_epsilon) / N, -math.asinh(1 / parameter_epsilon) / N]
		#poles = [[(-math.sin(x_) * math.sinh(y_), math.cos(x_) * math.cosh(y_)) for x_ in x] for y_ in y]
		if not normalized:
			omega_p = self.passband_frequency_high
			poles = [(s[0] * omega_p, s[1] * omega_p) for s in poles]
		# poles	= [s * omega_p for s in poles]

		return poles
