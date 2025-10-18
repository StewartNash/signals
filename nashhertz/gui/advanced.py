import tkinter as tk
from tkinter import ttk

class AdvancedFilter:
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
        pass
