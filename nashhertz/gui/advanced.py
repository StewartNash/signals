import tkinter as tk
from tkinter import ttk

class AdvancedFilter:
    FILTER_TYPES = [
        "Gaussian",
        "Bessel",
        "Butterworth",
        "Legendre",
        "Chebyshev I",
        "Chebyshev II",
        "Hourglass",
        "Elliptic",
        "Custom",
        "Raised Cos",
        "Matched",
        "Delay"
    ]
    FILTER_CLASSES = [
        "Low Pass",
        "High Pass",
        "Band Pass",
        "Band Stop",
        "Diplexer 1",
        "Diplexer 2"
    ]
    FREQUENCY_SCALES = ["Rad/Sec", "Hertz"]
    def __init__(self):
        pass

class AdvancedForm(ttk.Frame):
    def __init__(self, parent, model=None):
        super().__init__(parent)
        self.model = model
        if not self.model:
            self.model = AdvancedFilter()
        self.create_form()
        
    def create_form(self):
        self.left_frame = ttk.Frame(self)
        self.right_frame = ttk.Frame(self)
        
        self.left_upper_frame = ttk.Frame(self.left_frame)
        self.left_lower_frame = ttk.Frame(self.left_frame)
        self.right_upper_frame = ttk.Frame(self.right_frame)
        self.right_lower_frame = ttk.Frame(self.right_frame)
        
        self.filtertype_labelframe = tk.LabelFrame(self.left_upper_frame, text="Filter Type")
        self.filtertype_intvar = tk.IntVar(value=2)
        for index, text in enumerate(AdvancedFilter.FILTER_TYPES):
            radio_button = tk.Radiobutton(self.filtertype_labelframe, text=text, variable=self.filtertype_intvar, value=index)
            radio_button.pack(anchor="w")

        self.filterattributes_labelframe = tk.LabelFrame(self.left_upper_frame, text="Filter Attributes")
        self.standardattenuation_booleanvar = tk.BooleanVar(value=True)
        self.standardattenuation_checkbutton =  tk.Checkbutton(self.filterattributes_labelframe,
            text="Standard Pass Band Attenuation",
            command=self.generic_callback,
            variable=self.standardattenuation_booleanvar,
            onvalue=True,
            offvalue=False
        )
        self.setorder_button = tk.Button(self.filterattributes_labelframe, text="Set Order", command=self.generic_callback)
        self.order_stringvar = tk.StringVar()
        self.order_spinbox = tk.Spinbox(self.filterattributes_labelframe, from_=1.0, to=100.0, textvariable=self.order_stringvar)
        
        self.filterclass_labelframe = tk.LabelFrame(self.left_lower_frame, text="Filter Class")
        self.filterclass_intvar = tk.IntVar(value=0)
        self.multiplebands_booleanvar = tk.BooleanVar(value=False)
        for index, text in enumerate(AdvancedFilter.FILTER_CLASSES):
            radio_button = tk.Radiobutton(self.filterclass_labelframe, text=text, variable=self.filterclass_intvar, value=index)
            radio_button.pack(anchor="w")
        self.multiplebands_checkbutton = tk.Checkbutton(self.filterclass_labelframe,
            text="Multiple Bands",
            command=self.generic_callback,
            variable=self.multiplebands_booleanvar,
            onvalue=True,
            offvalue=False
        )
        
        self.freqscale_labelframe = tk.LabelFrame(self.left_lower_frame, text="Freq Scale")
        self.freqscale_intvar = tk.IntVar(value=1)
        self.log_booleanvar = tk.BooleanVar(value=True)
        for index, text in enumerate(AdvancedFilter.FREQUENCY_SCALES):
            radio_button = tk.Radiobutton(self.freqscale_labelframe, text=text, variable=self.freqscale_intvar, value=index)
            radio_button.pack(anchor="w")
        self.log_checkbutton = tk.Checkbutton(self.freqscale_labelframe,
            text="Log",
            command=self.generic_callback,
            variable=self.log_booleanvar,
            onvalue=True,
            offvalue=False
        )
        
        self.graphlimits_labelframe = tk.LabelFrame(self.left_lower_frame, text="Graph Limits")
        
        self.idealfilterresponse_labelframe = tk.LabelFrame(self.right_upper_frame, text="Ideal Filter Response")
        self.frequencyrepsonse_button = tk.Button(self.idealfilterresponse_labelframe, text="Frequency Resp.", command=self.generic_callback)
        self.transferfunction_button = tk.Button(self.idealfilterresponse_labelframe, text="Transfer Function", command=self.generic_callback)
        self.timeresponse_button = tk.Button(self.idealfilterresponse_labelframe, text="Time Response", command=self.generic_callback)
        self.polezeroplots_button = tk.Button(self.idealfilterresponse_labelframe, text="Pole Zero Plots", command=self.generic_callback)
        self.sparameters_button = tk.Button(self.idealfilterresponse_labelframe, text="S Parameters", command=self.generic_callback)
        
        self.lumpeddesign_labelframe = tk.LabelFrame(self.right_lower_frame, text="Lumped Design")
        self.lumpeddesign_notebook = ttk.Notebook(self.lumpeddesign_labelframe)
        self.topology_frame = ttk.Frame(self.lumpeddesign_notebook)
        self.parasitics_frame = ttk.Frame(self.lumpeddesign_notebook)
        self.nodesandleads_frame = ttk.Frame(self.lumpeddesign_notebook)
        
        self.topology_frame.pack(fill='both', expand=True)
        self.parasitics_frame.pack(fill='both', expand=True)
        self.nodesandleads_frame.pack(fill='both', expand=True)
        
        self.lumpeddesign_notebook.add(self.topology_frame, text="Topology")
        self.lumpeddesign_notebook.add(self.parasitics_frame, text="Parasitics")
        self.lumpeddesign_notebook.add(self.nodesandleads_frame, text="Nodes & Leads")

        self.standardattenuation_checkbutton.pack()
        self.setorder_button.pack()
        self.order_spinbox.pack()

        self.multiplebands_checkbutton.pack()
        self.log_checkbutton.pack()
        
        self.synthesizefilter_button = tk.Button(self.topology_frame, text="Synthesize Filter", command=self.generic_callback)
        self.synthesizefilter_button.pack()
        
        self.filtertype_labelframe.pack(side=tk.LEFT)
        self.filterattributes_labelframe.pack(side=tk.LEFT)
        
        self.frequencyrepsonse_button.grid(row=0, column=0)
        self.transferfunction_button.grid(row=1, column=0)
        self.timeresponse_button.grid(row=0, column=1)
        self.polezeroplots_button.grid(row=1, column=1)
        self.sparameters_button.grid(row=0, column=2)
        
        self.filterclass_labelframe.pack(side=tk.LEFT)
        self.freqscale_labelframe.pack(side=tk.LEFT)
        self.graphlimits_labelframe.pack(side=tk.LEFT)
        
        self.lumpeddesign_notebook.pack()
        
        self.idealfilterresponse_labelframe.pack(side=tk.RIGHT)
        self.lumpeddesign_labelframe.pack(side=tk.RIGHT)

        self.left_upper_frame.pack()
        self.left_lower_frame.pack()
        self.right_upper_frame.pack()
        self.right_lower_frame.pack()

        self.left_frame.pack(side=tk.LEFT)
        self.right_frame.pack(side=tk.LEFT)
        
    def generic_callback(self):
        pass
