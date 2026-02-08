import tkinter as tk
from tkinter import ttk

import numpy as np

from nashhertz.gui.utilities import TableView, Chart, CodeView
from signals.filter import FilterType, FilterWindow, FilterFamily
from signals.analog import ButterworthFilter, ChebyshevFilter, AnalogFilter


class FilterPlotView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.upper_frame = ttk.Frame(self)
        self.chart = Chart(self)
        chart_parameters = {
            "grid vertical lines" : 5,
            "grid horizontal lines" : 5
        }
        self.chart.set_parameters(chart_parameters)
        
        self.upper_frame.pack()
        self.chart.pack()
        
    def update(self, filter, graph_settings):
        frequencies = graph_settings['frequency']
        x, y = filter.magnitude_response(frequencies, is_db=True)
        self.chart.plot(x, y)


class QuickFilter:
    def __init__(self):
        self.frequencies = []
        self.resolution = 100
        self.filter = self.initialize_filter()
        self._observers = []
        
    def add_observer(self, function):
        self._observers.append(function)
        
    def notify(self):
        for function in self._observers:
            function()
            
    def update(self, parameters):
        self.filter.set_parameters(parameters)
        self.notify()
        
    def initialize_filter(self):
        filter = ButterworthFilter()
        filter_specifications = {
            "type" : FilterType.LOWPASS,
            "family" : FilterFamily.BUTTERWORTH,
            "passband attenuation" : 3.01, # dB
            "stopband attenuation" : 40, # dB
            "impedance" : 50, # Ohms
            #"passband frequency" : 1, # GHz
            #"stopband frequency" : 2, # GHz
            "passband frequency" : 1.0E9, # Hz
            "stopband frequency" : 2.0E9, # Hz
        }
        filter.set_parameters(filter_specifications)
        stopband_frequency = filter.stopband_frequency_low
        passband_frequency = filter.passband_frequency_high
        minimum_frequency = 0
        maximum_frequency = stopband_frequency + 0.5 * (stopband_frequency - passband_frequency)
        self.frequencies = np.linspace(minimum_frequency, maximum_frequency, self.resolution)
        
        return filter
    

class QuickFilterForm(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_form()
        self.controller = None

        # Sample data
        general_data = [
            ("passband attenuation", 3.01, "dB"),
            ("stopband attenuation", 40, "dB"),
            ("impedance", 50, "Ohm"),
            ("inductor Q", float('inf'), ""),
            ("capacitor Q", float('inf'), "")
        ]
        specific_data = [
            ("passband frequency", 1, "GHz"),
            ("stopband frequency", 2, "GHz")
        ]
        self.general_requirements_tableview.set_parameters(general_data)
        self.specific_requirements_tableview.set_parameters(specific_data)

    @classmethod
    def list_to_dictionary(cls, parameters):
        return {
            name: value
            for name, value, unit in parameters
        }

    def set_controller(self, controller):
        self.controller = controller
        self.specific_requirements_tableview.set_controller(controller)
        self.general_requirements_tableview.set_controller(controller)
        
    def on_change(self):
        parameters = self.read_form()
        self.controller.update_filter(parameters)
        
    def create_form(self):
        self.upper_frame = ttk.Frame(self)
        self.middle_frame = ttk.Frame(self)
        self.lower_frame = ttk.Frame(self)
        
        self.upper_upper_frame = ttk.Frame(self.upper_frame)
        self.upper_lower_frame = ttk.Frame(self.upper_frame)
        
        self.class_frame = ttk.Frame(self.upper_upper_frame)
        self.shape_frame = ttk.Frame(self.upper_upper_frame)
        self.update_frame = ttk.Frame(self.upper_lower_frame)
        self.implementation_frame = ttk.Frame(self.upper_lower_frame)
        
        #self.upper_class_frame = ttk.Frame(self.class_frame)
        #self.lower_class_frame = ttk.Frame(self.class_frame)
        #self.upper_shape_frame = ttk.Frame(self.shape_frame)
        #self.lower_shape_frame = ttk.Frame(self.shape_frame)
        #self.upper_update_frame = ttk.Frame(self.update_frame)
        #self.lower_update_frame = ttk.Frame(self.update_frame)
        #self.upper_implementation_frame = ttk.Frame(self.implementation_frame)
        #self.lower_implementation_frame = ttk.Frame(self.implementation_frame)

        self.lowpass_button = tk.Button(self.class_frame, text="Low Pass")
        self.highpass_button = tk.Button(self.class_frame, text="High Pass")
        self.bandpass_button = tk.Button(self.class_frame, text="Band Pass")
        self.bandstop_button = tk.Button(self.class_frame, text="Band Stop")

        self.bessel_button = tk.Button(self.shape_frame, text="Bessel")
        self.butterworth_button = tk.Button(self.shape_frame, text="Butterworth")
        self.chebyshev_1_button = tk.Button(self.shape_frame, text="Chebyshev I")
        self.chebyshev_2_button = tk.Button(self.shape_frame, text="Chebyshev II")
        self.elliptic_button = tk.Button(self.shape_frame, text="Elliptic")
        
        self.update_button = tk.Button(self.update_frame, text="Update")

        self.lumped_synthesis_button = tk.Button(self.implementation_frame, text="Lumped Synthesis")
        self.distributed_synthesis_button = tk.Button(self.implementation_frame, text="Distributed Synthesis")
        self.active_synthesis_button = tk.Button(self.implementation_frame, text="Active Synthesis")
        self.switched_capacitor_synthesis_button = tk.Button(self.implementation_frame, text="Switched Capacitor Synthesis")
        self.digital_synthesis_button = tk.Button(self.implementation_frame, text="Digital Synthesis")
        
        self.left_middle_frame = ttk.Frame(self.middle_frame) # Requirements
        self.right_middle_frame = ttk.Frame(self.middle_frame) # Topologies
        self.general_requirements_tableview = TableView(self.left_middle_frame)
        self.specific_requirements_tableview = TableView(self.left_middle_frame)
        self.topologies_label = tk.Label(self.right_middle_frame, text="Topologies: ")
        self.topologies_listbox = tk.Listbox(self.right_middle_frame)
        
        self.left_lower_frame = ttk.Frame(self.lower_frame)
        self.right_lower_frame = ttk.Frame(self.lower_frame)
        self.demo_text = CodeView(self.left_lower_frame)
        #self.results_chart = Chart(self.right_lower_frame)
        self.results_chart = FilterPlotView(self.right_lower_frame)
        
        self.topologies_label.pack()
        self.topologies_listbox.pack()
        self.general_requirements_tableview.pack(side=tk.LEFT)
        self.specific_requirements_tableview.pack()
        self.demo_text.pack()
        self.results_chart.pack()
        
        self.left_middle_frame.pack(side=tk.LEFT)
        self.right_middle_frame.pack(side=tk.LEFT)
        self.left_lower_frame.pack(side=tk.LEFT)
        self.right_lower_frame.pack(side=tk.LEFT)
        
        self.lowpass_button.pack(side=tk.LEFT)
        self.highpass_button.pack(side=tk.LEFT)
        self.bandpass_button.pack(side=tk.LEFT)
        self.bandstop_button.pack(side=tk.LEFT)

        self.bessel_button.pack(side=tk.LEFT)
        self.butterworth_button.pack(side=tk.LEFT)
        self.chebyshev_1_button.pack(side=tk.LEFT)
        self.chebyshev_2_button.pack(side=tk.LEFT)
        self.elliptic_button.pack(side=tk.LEFT)

        self.update_button.pack(side=tk.LEFT)

        self.lumped_synthesis_button.pack(side=tk.LEFT)
        self.distributed_synthesis_button.pack(side=tk.LEFT)
        self.active_synthesis_button.pack(side=tk.LEFT)
        self.switched_capacitor_synthesis_button.pack(side=tk.LEFT)
        self.digital_synthesis_button.pack(side=tk.LEFT)

        #self.upper_class_frame.pack()
        #self.lower_class_frame.pack()
        #self.upper_shape_frame.pack()
        #self.lower_shape_frame.pack()
        #self.upper_update_frame.pack()
        #self.lower_update_frame.pack()
        #self.upper_implementation_frame.pack()
        #self.lower_implementation_frame.pack()

        self.class_frame.pack(side=tk.LEFT)
        self.shape_frame.pack(side=tk.LEFT)
        self.update_frame.pack(side=tk.LEFT)
        self.implementation_frame.pack(side=tk.LEFT)
        
        #self.class_frame.grid(row=0, column=0, sticky="w")
        #self.shape_frame.grid(row=0, column=1, sticky="w")
        #self.update_frame.grid(row=1, column=0, sticky="w")
        #self.implementation_frame.grid(row=1, column=1, sticky="w")
        
        self.upper_upper_frame.pack()
        self.upper_lower_frame.pack()
        
        self.upper_frame.pack()
        self.middle_frame.pack()
        self.lower_frame.pack()
        
    def update_form(self):
        pass


class QuickFilterController:
    UNIT_SCALE = {
        "HZ": 1, "KHZ": 1E3, "MHZ": 1E6, "GHZ": 1E9,
        "OHM": 1, "KOHM": 1E3, "MOHM": 1E6,
        "F": 1, "UF": 1E-6, "NF": 1E-9, "PF": 1E-12,
        "H": 1, "MH": 1E-3, "UH": 1E-6, "NH": 1E-9, "PH": 1E-12
    }
    def __init__(self, model, view, plot):
        self.model = model
        self.view = view
        self.plot = plot
        
        self.view.set_controller(self)
        self.model.add_observer(self.on_change)
        self.model.notify()

    @classmethod
    def list_to_dictionary(cls, parameters):
        result = {}
        for name, value, unit in parameters:
            try:
                value = float(value)
            except ValueError:
                pass
            if unit:
                scale = cls.UNIT_SCALE.get(unit.upper(), 1)
                value *= scale                
            result[name] = value

        return result

    def get_parameters(self):
        parameter_list_general = self.view.general_requirements_tableview.get_parameters()
        parameter_list_specific = self.view.specific_requirements_tableview.get_parameters()
        parameter_dictionary_general = self.list_to_dictionary(parameter_list_general)
        parameter_dictionary_specific = self.list_to_dictionary(parameter_list_specific)
        if "passband frequency" in parameter_dictionary_specific:
            pass  # What code goes here to convert frequency?
        filter_specifications = {
            "type": FilterType.LOWPASS,
            "family": FilterFamily.BUTTERWORTH,
            #"passband attenuation" : 3.01, # dB
            #"stopband attenuation" : 40, # dB
            "impedance": 50,  # Ohms
            #"passband frequency" : 1.0E9, # Hz
            #"stopband frequency" : 2.0E9, # Hz
        }
        parameters = {}
        for d in (
                parameter_dictionary_general,
                parameter_dictionary_specific,
                filter_specifications):
            parameters.update(d)

        return parameters

    def update_filter(self, parameters):
        if parameters["family"] == FilterFamily.BUTTERWORTH:
            self.model.filter = ButterworthFilter()
        elif parameters["family"] == FilterFamily.CHEBYSHEV:
            self.model.filter = ChebyshevFilter()
        else:
            self.model.filter = AnalogFilter()
        self.model.filter.set_parameters(parameters)
        graph_settings = {}
        graph_settings['frequency'] = self.model.frequencies
        self.plot.update(self.model.filter, graph_settings)
        
    def on_change(self):
        parameters = self.get_parameters()

        self.update_filter(parameters)

    #def on_change_table(self, row, column, value):
    #    pass
        


