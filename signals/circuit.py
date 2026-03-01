from signals.filter import Filter
from signals.utility import Polynomial, RationalFunction
from signals.Analog import ButterworthFilter
import data.constants

import enum
import numpy as np


class ComponentType(enum.Enum):
	RESISTOR = 1
	CAPACITOR = 2
	INDUCTOR = 3
	VOLTAGE_SOURCE = 4
	CURRENT_SOURCE = 5
	

class Component:
    #def __init__(self, component_type, value_pair):
    def __init__(self, component_type, value):
        self.component_type = component_type
        self.value = value
        
    @classmethod
    def component(cls, component_pair):
        value = component_pair[0]
        component_type = component_pair[1]
        if component_type == "resistor":
            return Component(ComponentType.RESISTOR, value)
        elif component_type == "capacitor":
            return Component(ComponentType.CAPACITOR, value)
        elif component_type == "inductor":
            return Component(ComponentType.INDUCTOR, value)
        elif component_type == "voltage source"
            return Component(ComponentType.VOLTAGE_SOURCE, value)
        elif component_type == "current source"
            return Component(ComponentType.CURRENT_SOURCE, value)
        else:
            raise ValueError("Unknown component value")


class Circuit:
    def __init__(self):
        pass
        

class FilterCircuit(Circuit):
    def __init__(self, filter):
        self.filter = filter
        
    def get_circuit(self):
        pass
      
    @classmethod
    def butterworth_prototypes(cls, order):
        g = []
        n = order
        for k in range(1, n + 1):
            value = 2 * np.sin((2 * k - 1) * np.pi / (2 * n))
            g.append(value)
        
        return g

    @classmethod
    def butterworth_ladder(cls, order, impedance, cutoff_frequency):
        g = butterworth_prototypes(order)
        elements = []
        for i, g_k in enumerate(g):
            if i % 2 == 0: # series L
                inductance = impedance   * g_k / cutoff_frequency
                elements.append(("L", inductance))
            else: # shunt C
                capacitance = g_k / (impedance * cutoff_frequency)
                elements.append(("C", capacitance))

        return elements
        
def driving_point_impedance(poles, zeros, load):
    if zeros is None:
        zeros = [1]
        numerator = Polynomial(values=zeros, is_coefficients=True)
    else:
        numerator = Polynomial(values=zeros, is_coefficients=False)
    denominator = Polynomial(values=poles, is_coefficients=False)
    transfer_function = RationalFunction(numerator, denominator)
    load_impedance = Polynomial(load)
    unity = Polynomial(1)
    load_impedance = RationalFunction(load_impedance, unity)
    impedance = (load_impedance - load_impedance * transfer_function) / transfer_function
    
    return impedance
    
def ladder_elements(impedance):
    return impedance.continued_fraction
    
if __name__ == "__main__":
        filter = ButterworthFilter()
        frequency_stopband = 2.0E9 # Hz
        frequency_passband = 1.0E9 # Hz
        omega_s = 2 * np.pi * frequency_stopband
        omega_p = 2 * np.pi * frequency_passband
        filter_specifications = {
            "type" : FilterType.LOWPASS,
            "family" : FilterFamily.BUTTERWORTH,
            "passband attenuation" : 3.01, # dB
            "stopband attenuation" : 40, # dB
            "impedance" : 1, # Normalized impedance
            "passband frequency" : 1 / (2 * np.pi) # Normalized frequency
            "stopband frequency" : omega_s / omega_p / (2 * np.pi)
        }
        filter.set_parameters(filter_specifications)
        poles = filter.get_poles()
        zeros = None
        load = 50
        impedance = driving_point_impedance(poles, zeros, load)
        ladder = ladder_elements(impedance)

