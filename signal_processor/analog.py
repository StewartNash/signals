import math

from signal_processor.filter import FilterType, FilterWindow, Filter


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
	
	passband_frequency = pass_band_frequency_high
	stopband_frequency = stopband_frequency_low
	omega_p = passband_frequency
	omega_s = stopband_frequency
	
	parameter_k0 = omega_p / omega_s
	filter_order = int(math.log10(A) / math.log10(1 / parameter_k0))
	
	return (filter_order, parameter_epsilon)	

def bessel_filter_order(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	specified_passband_ripple,
	minimum_stopband_attenuation):

	#transition_bandwidth_low  = abs(passband_frequency_high - stopband_frequency_high)
	#transition_bandwidth_high = abs(passband_frequency_low - stopband_frequency_low)
    #
	#if filter_type == FilterType.LOWPASS:
	#	transition_bandwidth = transition_bandwidth_low
	#elif filter_type == FilterType.HIGHPASS:
	#	transition_bandwidth = transition_bandwidth_high
	#elif filter_type in (FilterType.BANDPASS, FilterType.BANDSTOP):
	#	transition_bandwidth = min(transition_bandwidth_low, transition_bandwidth_high)
	#else:
	#	raise ValueError("Unsupported filter type")
    #
	#delta_stopband = 10 ** (-0.05 * minimum_stopband_attenuation)
	#delta_passband = (10 ** (0.05 * specified_passband_ripple) - 1) / (10 ** (0.05 * specified_passband_ripple) + 1)
	#delta = min(delta_passband, delta_stopband)
	#minimum_stopband_attenuation = -20 * math.log10(delta)
    #
	#if minimum_stopband_attenuation <= 21:
	#	parameter_d = 0.9222
	#else:
	#	parameter_d = (minimum_stopband_attenuation - 7.95) / 14.36
	#	
	#filter_order = int(2 + parameter_d * sampling_frequency / transition_bandwidth)
	#if filter_order % 2 == 0:
	#	filter_order += 1  # Make it odd
    #
	#return (filter_order, delta, minimum_stopband_attenuation, parameter_d)

    filter_order, parameter_epsilon = bessel_filter_coefficients(filter_type,
	passband_frequency_low,
	passband_frequency_high,
	stopband_frequency_low,
	stopband_frequency_high,
	specified_passband_ripple,
	minimum_stopband_attenuation)
	
	return filter_order


class AnalogFilter(Filter):
    def __init__(self):
        super().__init__()
        
    def magnitude_response(self, frequencies):
        #frequencies = []
        magnitudes = []
        if self.family is FilterFamily.BESSEL:
            filter_order, parameter_epsilon = bessel_filter_coefficients(
                self.type,
	            self.passband_frequency_low,
	            self.passband_frequency_high,
	            self.stopband_frequency_low,
	            self.stopband_frequency_high,
	            self.specified_passband_ripple,
	            self.stopband_attenuation
	        )
	        omega_p = self.passband_frequency_high
	        magnitudes = [1 / (1 + parameter_epsilon ** 2 * (omega / omega_p) ** (2 * filter_order)) for omega in frequencies]
        return (frequencies, magnitudes)
        

