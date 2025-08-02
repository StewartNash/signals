import unittest
from signal_processor.infinite_impulse_response import compute_filter_order, lowpass_computations, FilterType, FilterFamily
from signal_processor.infinite_impulse_response import butterworth_analog_poles


class TestIir(unittest.TestCase):
	TOLERANCE = 0.0000005
	
	def test_butterworth_analog_poles(self):
		# Example 4.A.1
		# s-plane poles (real, imaginary)
		s_plane_poles = [
			(-0.1564345, 0.9876885),
			(-0.4539906, 0.8910065),
			(-0.7071068, 0.7071067),
			(-0.8910066, 0.4539905),
			(-0.9876884, 0.1564344)
		]
		N = 2 * len(s_plane_poles)
		results = butterworth_analog_poles(N)
		for i in range(int(N / 2)):
			self.assertLess(abs(results[i][0] - s_plane_poles[i][0]), TestIir.TOLERANCE, "S plane pole out of tolerance")
			self.assertLess(abs(results[i][1] - s_plane_poles[i][1]), TestIir.TOLERANCE, "S plane pole out of tolerance")

if __name__ == "__main__":
	unittest.main()

