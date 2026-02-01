import math
from abc import ABC, abstractmethod

from signal_processor.filter import FilterType, FilterWindow, Filter, FilterFamily


def bessel_filter_coefficients(filter_type,
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

def bessel_filter_order(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	specified_passband_ripple,
	minimum_stopband_attenuation):

	filter_order, parameter_epsilon = bessel_filter_coefficients(
	    filter_type,
	    passband_frequency_low,
	    passband_frequency_high,
	    stopband_frequency_low,
	    stopband_frequency_high,
	    specified_passband_ripple,
	    minimum_stopband_attenuation
	)
	
	return filter_order


class AnalogFilter(Filter, ABC):
	def __init__(self):
		super().__init__()

	@abstractmethod
	def magnitude_response(self, frequencies, is_db=False):
		#frequencies = []
		magnitudes = []
		if self.family is FilterFamily.BUTTERWORTH:
			filter_order, parameter_epsilon = bessel_filter_coefficients(
				self.type,
				self.passband_frequency_low,
				self.passband_frequency_high,
				self.stopband_frequency_low,
				self.stopband_frequency_high,
				self.specified_passband_ripple,
				self.minimum_stopband_attenuation
			)
			omega_p = self.passband_frequency_high
			magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order))) for omega in frequencies]
			if is_db:
				magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)


class ButterworthFilter(AnalogFilter):
	def __init__(self):
		super().__init__()

	def magnitude_response(self, frequencies, is_db=False):
		# frequencies = []
		magnitudes = []
		if self.family is FilterFamily.BUTTERWORTH:
			filter_order, parameter_epsilon = bessel_filter_coefficients(
				self.type,
				self.passband_frequency_low,
				self.passband_frequency_high,
				self.stopband_frequency_low,
				self.stopband_frequency_high,
				self.specified_passband_ripple,
				self.minimum_stopband_attenuation
			)
			omega_p = self.passband_frequency_high
			magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order))) for
						  omega in frequencies]
			if is_db:
				magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)

class ChebyshevFilter(AnalogFilter):
	def __init__(self):
		super().__init__()

	def magnitude_response(self, frequencies, is_db=False):
		# frequencies = []
		magnitudes = []
		if self.family is FilterFamily.BUTTERWORTH:
			filter_order, parameter_epsilon = bessel_filter_coefficients(
				self.type,
				self.passband_frequency_low,
				self.passband_frequency_high,
				self.stopband_frequency_low,
				self.stopband_frequency_high,
				self.specified_passband_ripple,
				self.minimum_stopband_attenuation
			)
			omega_p = self.passband_frequency_high
			magnitudes = [math.sqrt(1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order))) for
						  omega in frequencies]
			if is_db:
				magnitudes = [20 * math.log10(h) for h in magnitudes]

		return (frequencies, magnitudes)
