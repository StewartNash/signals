# Plot sum-of-three-sines in the time and frequency domains (complex)
# - This exercise is very similar to Exercise 5.1. Here you will run a 
#   MATLAB script to plot the signal from Eq. (5.8) in the time and 
#   frequency domains. This time however, we will focus on the complex
#   frequency domain. 
import numpy as np

# set parameters
fs = 10240                     # sampling rate
T_max = 1.0                    # sim end time
t = np.arange(0, T_max, 1/fs)  # time vector
#t = t.reshape(-1, 1)
f1 = 100                       # frequency of 1st tone 
f2 = 200                       # frequency of 2nd tone 
f3 = 300                       # frequency of 3rd tone
A1 = 10                        # amplitudes of tones 1, 2, 3...
A2 = 1
A3 = 4
