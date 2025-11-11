import unittest
from signal_processor.infinite_impulse_response import compute_filter_order, hplp_parameters, lowpass_parameters, FilterType, FilterFamily
from signal_processor.infinite_impulse_response import butterworth_analog_poles, chebyshev_analog_poles
from data.ex_4_a_1 import ex_4_a_1_constants
from data.ex_4_a_2 import ex_4_a_2_constants

class TestIir(unittest.TestCase):
	TOLERANCE = 0.0000005
	
	def test_butterworth_analog_poles(self):
		# Example 4.A.1
		s_plane_poles = ex_4_a_1_constants["s_plane_poles"]
		s_plane_poles = sorted(s_plane_poles, key=lambda x: (x[0], x[1]), reverse=True)
		N = 2 * len(s_plane_poles)
		results = butterworth_analog_poles(N)
		results = sorted(results, key=lambda x: (x[0], x[1]), reverse=True)
		for i in range(int(N / 2)):
			self.assertLess(abs(results[i][0] - s_plane_poles[i][0]), TestIir.TOLERANCE, "S plane pole out of tolerance")
			self.assertLess(abs(results[i][1] - s_plane_poles[i][1]), TestIir.TOLERANCE, "S plane pole out of tolerance")

	def test_chebyshev_analog_poles(self):
		# Example 4.A.2
		s_plane_poles = ex_4_a_2_constants["s_plane_poles"]
		s_plane_poles = sorted(s_plane_poles, key=lambda x: (x[0], x[1]), reverse=True)
		K_, A_, epsilon_, lambda_ = hplp_parameters(ex_4_a_2_constants["Ap"],
			ex_4_a_2_constants["As"],
			ex_4_a_2_constants["fp2"],
			ex_4_a_2_constants["fs2"],
			ex_4_a_2_constants["F"])		
		N = len(s_plane_poles)
		results = chebyshev_analog_poles(N, epsilon_)
		results = sorted(results, key=lambda x: (x[0], x[1]), reverse=True)
		#print("-------------")
		#print("s-plane poles")
		#print("-------------")
		#for pole in s_plane_poles:
		#	print(pole)
		#print("------------------------")
		#print("Calculated s-plane poles")
		#print("------------------------")
		#for pole in results:
		#	print(pole)
		for i in range(int(N / 2)):
			self.assertLess(abs(results[i][0] - s_plane_poles[i][0]), TestIir.TOLERANCE, "S plane pole out of tolerance")
			self.assertLess(abs(results[i][1] - s_plane_poles[i][1]), TestIir.TOLERANCE, "S plane pole out of tolerance")

if __name__ == "__main__":
	unittest.main()

