from signals.filter import Filter
import data.constants

import enum


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
