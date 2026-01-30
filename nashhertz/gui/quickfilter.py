import tkinter as tk
from tkinter import ttk

from nashhertz.gui.utilities import TableView, Chart, CodeView
from signal_processor.filter import FilterType, FilterWindow, Filter, FilterFamily

class QuickFilter:
    def __init__(self):
        self.filter = self.initialize_filter()
        
    def initialize_filter(self):
        filter = Filter()
        filter_specifications = {
            "type" : FilterType.LOWPASS,
            "family" : FilterFamily.BUTTERWORTH,
            "passband attenuation" : 3.01, # dB
            "stopband attenuation" : 40, # dB
            "impedance" : 50, # Ohms
            "passband frequency" : 1, # GHz
            "stopband frequency" : 2, # GHz
        }
        filter.set_parameters(filter_specifications)
        return filter
        
    def graph_filter(self):
        pass        
    

class QuickFilterForm(ttk.Frame):
    def __init__(self, parent, model=None):
        super().__init__(parent)
        self.model = model
        if not self.model:
            self.model = QuickFilter()
        self.create_form()
        
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
        self.results_chart = Chart(self.right_lower_frame)
        
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
