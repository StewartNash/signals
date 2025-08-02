import unittest
from signal_processor.finite_impulse_response import kaiser_filter_order, kaiser_coefficients, FilterType
from .fir_constants import ex_5_6_constants

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

class TestFir(unittest.TestCase):
	TOLERANCE = 0.0000005
	
	def test_kaiser_lowpass(self):
		# Example 5.6 - Lowpass FIR filter
		temporary = ex_5_6_constants["fir_coefficients"]
		causal_index, non_causal_index, hd, ak, h = zip(*[(x[0], x[1], x[2], x[3], x[4]) for x in temporary])
		causal_index, non_causal_index, hd, ak, h = list(causal_index), list(non_causal_index), list(hd), list(ak), list(h)
		
		# Get Kaiser coefficients
		passband_frequency_low = 120
		passband_frequency_high = 180
		specified_passband_ripple = 0.5
		stopband_frequency_low = 60
		stopband_frequency_high = 240
		minimum_stopband_attenuation = 35
		sampling_frequency = 600

		filter_type = FilterType.BANDPASS

		filter_order, delta, minimum_stopband_attenuation, parameter_d = kaiser_filter_order(filter_type,
			passband_frequency_low,
			passband_frequency_high,
			stopband_frequency_low,
			stopband_frequency_high,
			sampling_frequency,
			specified_passband_ripple,
			minimum_stopband_attenuation)

		kaiser_coeffs, alpha = kaiser_coefficients(filter_order, minimum_stopband_attenuation)
		
		# Test Kaiser coefficients
		for i in range(filter_order):
			self.assertLess(abs(kaiser_coeffs[i] - ak[i]), TestFir.TOLERANCE, "Kaiser coefficients out of tolerance")

if __name__ == "__main__":
	unittest.main()

