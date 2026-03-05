# Signals

This is a signal processing library. It contains signal processing algorithms. The focus of this signal processing library is mainly digital signal processing (DSP), but there is also an extensive collection of analog signal processing.

## NashHertz Filters

This package contains a filter design application. In order to run, issue the following command:
```
user@computer:~/signals$ python3 -m nashhertz.main
```

This application will be segregated to its own repository in the future.

### Instructions

A guide or instruction manual to using NashHertz Filters will be placed here.

## Modules

The DSP library consists of numerous modules. The modules are described here after instruction on use of the library.

### Instructions

Library use is demonstrated by examples. Examples are primarily in the examples module. Examples of running unit tests and examples are given below.

#### Unit testing

```
user@computer:~/signals$ python3 -m unittest discover tests
user@computer:~/signals$ python3 -m unittest discover -s tests -p 'test_*.py'
```

#### Running examples
```
user@computer:~/signals$ python3 -m examples.examples_3_2_7_iir
```

### Infinite Impulse Response

The 'infinite_impulse_response' module contains algorithms for infinite impulse response (IIR) filters.

### Finite Impulse Response

The 'finite_impulse_response' module contains algorithms for finite impulse response (FIR) filters.

### Fast Fourier Transform

The 'fast_fourier_transform' module contains implementations of the fast fourier transform (FFT).

### Multirate Processing

The 'multirate_processing' module contains examples and abstract implementations of multirate DSP processes. This comprises decimation and interpolation.

### Linear System Noise Response

The 'noise_response' module contains examples and abstract implementations of arbitrary linear systems constructed in the library #to noise.
 
### Truncation Effects

The 'truncation_effects' module contains examples and abstract implementations examining the effect of finite register lengths.

### Analog

The 'analog' module contains analog filters.

### Circuits

Contains circuit representations.

## SDR

The 'sdr' folder contains examples from 'Software Defined Radio using MATLAB & Simulink and the RTL-SDR' by Bob Stewart et al. The examples have been translated from MATLAB to Python. (ASIDE: I may transfer these files to a separate SDR repository in the future. I am not sure if it should be integrated with this repository. Though I could imagine it calling this repository extensively as a library. I am not sure what to do about Simulink translations. This may require a separate library. But I had a controls library that I was working on that may be able to hold this. For now, I think I may just make rudimentary block in Python to cobble the Simulink functionality together.)

## TODO
(This TODO list needs to be updated.)
- Finish unit tests
- Finish IIR filter examples
- Finish FIR filter examples
- Add FFT algorithms
- Create Filter class
	- Passband frequencies, stopband frequencies
