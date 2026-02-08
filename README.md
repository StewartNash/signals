# Signals

This is a signal processing library. It contains signal processing algorithms. Currently, the signal processing is exclusively digital signal processing (DSP).

## NashHertz Filters

This package contains a filter design application. In order to run, issue the following command:
```
user@computer:~/signals$ python3 -m nashhertz.main
```

This application will be segregated to its own repository in the future.

## Infinite Impulse Response

The 'infinite_impulse_response' module contains algorithms for infinite impulse response (IIR) filters.

## Finite Impulse Response

The 'finite_impulse_response' module contains algorithms for finite impulse response (FIR) filters.

## Fast Fourier Transform

The 'fast_fourier_transform' module contains implementations of the fast fourier transform (FFT).

## Multirate Processing

The 'multirate_processing' module contains examples and abstract implementations of multirate DSP processes. This comprises decimation and interpolation.

## Linear System Noise Response

The 'noise_response' module contains examples and abstract implementations of arbitrary linear systems constructed in the library to noise.
 
## Truncation Effects

The 'truncation_effects' module contains examples and abstract implementations examining the effect of finite register lengths.

## Analog

The 'analog' module contains analog filters.

## SDR

The 'sdr' folder contains examples from 'Software Defined Radio using MATLAB & Simulink and the RTL-SDR' by Bob Stewart et al. The examples have been translated from MATLAB to Python. (ASIDE: I may transfer these files to a separate SDR repository in the future. I am not sure if it should be integrated with this repository. Though I could imagine it calling this repository extensively as a library. I am not sure what to do about Simulink translations. This may require a separate library. But I had a controls library that I was working on that may be able to hold this. For now, I think I may just make rudimentary block in Python to cobble the Simulink functionality together.)

## Unit testing

```
user@computer:~/signals$ python3 -m unittest discover tests
user@computer:~/signals$ python3 -m unittest discover -s tests -p 'test_*.py'
```

## Running examples
```
user@computer:~/signals$ python3 -m examples.examples_3_2_7_iir
```

## TODO
- Finish unit tests
- Finish IIR filter examples
- Finish FIR filter examples
- Add FFT algorithms
- Create Filter class
	- Passband frequencies, stopband frequencies
