import tkinter as tk
from tkinter import ttk

#import math

class TableView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Define the table columns
        columns = ("Requirements", "Value", "Unit")
        # Create Treeview widget
        tree = ttk.Treeview(self, columns=columns, show='headings')
        # Define column properties (headers and width)
        tree.heading("Requirements", text="Requirements")
        tree.heading("Value", text="Value")
        tree.heading("Unit", text="Unit")
        
        tree.column("Requirements", width=150, anchor='center')
        tree.column("Value", width=50, anchor='w')
        tree.column("Unit", width=100, anchor='center')
        
        # Add sample data to Treeview
        data = [
            ("Passband Attenuation", 30, "dB"),
            ("Stopband Attenuation", 40, "dB"),
            ("Impedance", 50, "Ohms"),
            ("Inductor Q", float('inf'), "None"),
            ("Capacitor Q", float('inf'), "None")
        ]
        for row in data:
            tree.insert("", tk.END, values=row)
            
        # Add vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        # Layout Treeview and scrollbar
        tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
        ## Allow table resizing with window
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure(0, weight=1)

class CodeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Create Text widget
        text_widget = tk.Text(self, width=50, height=15)
        text_widget.pack(padx=10, pady=10)
        
        # Insert text
        sample_text = """
        The quick brown fox jumps over the
        lazy dog.
        """
        text_widget.insert(tk.END, sample_text)

class Chart(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Sample data
        data = {"A": 40, "B": 70, "C": 30, "D": 85}
        
        # Create Canvas widget
        canvas = tk.Canvas(self, width=400, height=300, bg="white")
        canvas.pack()
        
        # Draw graph
        bar_width = 50
        spacing = 20
        x_start = 50
        y_base = 250
        
        for i, (label, value) in enumerate(data.items()):
            # Calculate bar coordinates
            x1 = x_start + (bar_width + spacing) * i
            y1 = y_base - value
            x2 = x1 + bar_width
            y2 = y_base
            
            # Draw the bar
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            # Add label below bar
            canvas.create_text((x1 + x2) / 2, y_base + 10, text=label, anchor="n")
            # Add the value above the bar
            canvas.create_text((x1 + x2) / 2, y1  - 10, text=str(value), anchor="s")
        
