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
        
        self.filtertype_intvar = tk.IntVar(value=2)
        self.filtertype_labelframe = tk.LabelFrame(self.left_upper_frame, text="Filter Type")
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
        
        self.standardattenuation_checkbutton.pack()
        self.setorder_button.pack()
        self.order_spinbox.pack()
        
        self.filtertype_labelframe.pack(side=tk.LEFT)
        self.filterattributes_labelframe.pack(side=tk.LEFT)
        
        self.left_upper_frame.pack()
        self.left_lower_frame.pack()

        self.left_frame.pack(side=tk.LEFT)
        self.right_frame.pack(side=tk.LEFT)
        
    def generic_callback(self):
        pass
