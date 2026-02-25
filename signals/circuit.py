from signals.filter import Filter
from signals.Analog import ButterworthFilter
import data.constants

import numpy as np
import nump.polynomial.polynomial as poly
import enum


class Polynomial:
    def __init__(self, values, is_coefficients=True):
        if is_coefficients:
            self.set_coefficients(values)
        else:
            self.set_roots(values)

    def __repr__(self):
        return f"Polynomial({self.coefficients})"

    def get_roots(self):
        return np.roots(self.coefficients)

    def get_coefficients(self):
        return self.coefficients

    def set_roots(self, values):
        self.roots = values
        self.coefficients = np.poly(self.roots)

    def set_coefficients(self, values):
        self.coefficients = np.array(values, dtype=float)

    # -----------------
    # Arithmetic
    # -----------------

    def __add__(self, other):
        return Polynomial(np.polyadd(self.coefficients, other.coefficients))

    def __sub__(self, other):
        return Polynomial(np.polysub(self.coefficients, other.coefficients))

    def __mul__(self, other):
        return Polynomial(np.polymul(self.coefficients, other.coefficients))

    def __truediv__(self, other):
        """
        Polynomial long division
        Returns (quotient, remainder)
        """
        q, r = np.polydiv(self.coefficients, other.coefficients)
        return Polynomial(q), Polynomial(r)

    # -----------------
    # Polynomial GCD
    # -----------------

    @staticmethod
    def gcd(p1, p2, tol=1e-12):
        """
        Euclidean algorithm for polynomial GCD
        """
        a = Polynomial(p1.coefficients.copy())
        b = Polynomial(p2.coefficients.copy())

        while np.any(np.abs(b.coefficients) > tol):
            _, r = a / b
            a, b = b, r

        # Normalize leading coefficient to 1
        if abs(a.coefficients[0]) > tol:
            a.coefficients = a.coefficients / a.coefficients[0]

        return a


class RationalFunction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"RationalFunction({self.numerator}, {self.denominator})"

    # -----------------
    # Arithmetic
    # -----------------

    def __add__(self, other):
        num = (self.numerator * other.denominator +
               other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalFunction(num, den).reduce()

    def __sub__(self, other):
        num = (self.numerator * other.denominator -
               other.numerator * self.denominator)
        den = self.denominator * other.denominator
        return RationalFunction(num, den).reduce()

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return RationalFunction(num, den).reduce()

    def __truediv__(self, other):
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return RationalFunction(num, den).reduce()

    # -----------------
    # Rational Reduction
    # -----------------

    def reduce(self):
        gcd_poly = Polynomial.gcd(self.numerator, self.denominator)
        q_num, _ = self.numerator / gcd_poly
        q_den, _ = self.denominator / gcd_poly
        return RationalFunction(q_num, q_den)

    # -----------------
    # Continued Fraction Expansion
    # -----------------

    def continued_fraction(self):
        """
        Cauer continued fraction expansion.

        Returns list of Polynomial quotients.
        Useful for ladder extraction.
        """

        num = Polynomial(self.numerator.coefficients.copy())
        den = Polynomial(self.denominator.coefficients.copy())

        expansion = []

        while np.any(np.abs(den.coefficients) > 1e-12):
            q, r = num / den
            expansion.append(q)
            num, den = den, r

        return expansion
      


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
        filter_specifications = {
            "type" : FilterType.LOWPASS,
            "family" : FilterFamily.BUTTERWORTH,
            "passband attenuation" : 3.01, # dB
            "stopband attenuation" : 40, # dB
            "impedance" : 50, # Ohms
            "passband frequency" : 1 / (2 * np.pi), # Hz
            "stopband frequency" : 1 / (2 * np.pi# Hz
        }
        filter.set_parameters(filter_specifications)
        poles = filter.get_poles()
        zeros = None
        load = 50
        impedance = driving_point_impedance(poles, zeros, load)
        ladder = ladder_elements(impedance)
        
    
