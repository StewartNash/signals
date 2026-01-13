# Plot sum-of-three-sines in the time and frequency domains (complex)
# - This exercise is very similar to Exercise 5.1. Here you will run a 
#   MATLAB script to plot the signal from Eq. (5.8) in the time and 
#   frequency domains. This time however, we will focus on the complex
#   frequency domain. 
import numpy as np
import matplotlib.pyplot as plt

# --------------------
# set parameters
# --------------------
fs = 10240            # sampling rate (Hz)
T_max = 1.0           # simulation end time (seconds)

t = np.arange(0, T_max, 1/fs)   # time vector
#t = t.reshape(-1, 1)
f1 = 100              # frequency of 1st tone (Hz)
f2 = 200              # frequency of 2nd tone (Hz)
f3 = 300              # frequency of 3rd tone (Hz)

A1 = 10               # amplitudes of tones
A2 = 1
A3 = 4

# --------------------
# create sum of cosines signal
# --------------------
s_t = (
    A1 * np.cos(2 * np.pi * f1 * t)
    + A2 * np.cos(2 * np.pi * f2 * t)
    + A3 * np.cos(2 * np.pi * f3 * t)
)

# --------------------
# perform FFT using rectangular window
# --------------------
Nfft = 1024

X_1 = (1 / (2 * fs)) * np.fft.fftshift(np.fft.fft(s_t, Nfft))

f = np.arange(-Nfft//2, Nfft//2) / Nfft * fs   # frequency scale

# --------------------
# plot figure (time domain)
# --------------------
plt.figure(101)
plt.plot(t, s_t, 'b-', linewidth=2)
plt.axis([0, 0.03, -20, 20])
plt.xlabel('time (s)')
plt.ylabel('amplitude')
plt.title('Time Domain')
plt.grid(True)

# --------------------
# plot figure (frequency domain, 2-sided)
# --------------------
plt.figure(102)
#plt.stem(
#    f,
#    20 * np.real(X_1),
#    linefmt='r-',
#    markerfmt='ro',
#    basefmt=' ',
#    use_line_collection=True
#)
plt.stem(
    f,
    20 * np.real(X_1),
    linefmt='r-',
    markerfmt='ro',
    basefmt=' '
)
plt.axis([-400, 400, 0, 11])
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude')
plt.title('FFT with rectangular window')
plt.grid(True)

plt.show()

