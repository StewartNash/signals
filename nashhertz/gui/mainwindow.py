import tkinter as tk
from tkinter import ttk

from nashhertz.gui.quickfilter import QuickFilterForm
from nashhertz.gui.advanced import AdvancedForm

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NashHertz Filters")
        self.geometry("1080x720")
        self.create_menu()
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)
        self.forms = {}
        
        self.forms['QuickFilter'] = QuickFilterForm(self.main_frame)
        self.forms['Advanced'] = AdvancedForm(self.main_frame)
        
        for form in self.forms.values():
            form.grid(row=0, column=0, sticky='NSEW')
            
        self.show_form('QuickFilter')
        
        display_notice = True
        if display_notice:
            self.notice_window = NoticeWindow(self)
            #self.wait_window(self.notice_form)
        else:
            self.notice_form = None

    def show_form(self, name):
        form = self.forms[name]
        form.tkraise()
            
    def create_menu(self):
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Open', command=self.generic_callback)
        self.file_menu.add_command(label='Save', command=self.generic_callback)
        self.file_menu.add_command(label='Save As...', command=self.generic_callback)
        self.example_menu = tk.Menu(self.file_menu, tearoff=0)
        self.example_menu.add_command(label='Lumped', command=self.generic_callback)
        self.example_menu.add_command(label='Distributed', command=self.generic_callback)
        self.example_menu.add_command(label='Active', command=self.generic_callback)
        self.example_menu.add_command(label='Matching Networks', command=self.generic_callback)
        self.file_menu.add_cascade(label='Examples', menu=self.example_menu, underline=0)
        self.file_menu.add_command(label='Exit', command=self.destroy)
        self.menubar.add_cascade(label='File', menu=self.file_menu, underline=0)
        
        self.menubar.add_command(label='Zmatch', command=self.generic_callback)
        self.menubar.add_command(label='Data', command=self.generic_callback)
        
        self.options_menu = tk.Menu(self.menubar, tearoff=0)
        self.options_menu.add_command(label='Options Panel', command=self.generic_callback)
        self.options_menu.add_command(label='Initialization', command=self.generic_callback)
        self.options_menu.add_command(label='Colors', command=self.generic_callback)
        self.menubar.add_cascade(label='Options', menu=self.options_menu, underline=0)
        
        self.window_menu = tk.Menu(self.menubar, tearoff=0)
        self.window_menu.add_command(label='Cascade', command=self.generic_callback)
        self.window_menu.add_command(label='Tile Horizontally', command=self.generic_callback)
        self.window_menu.add_command(label='Tile Vertically', command=self.generic_callback)
        self.window_menu.add_command(label='Minimize All', command=self.generic_callback)
        self.window_menu.add_command(label='Normalize All', command=self.generic_callback)
        self.window_menu.add_command(label='Close All', command=self.generic_callback)
        self.window_menu.add_command(label='Floating Windows', command=self.generic_callback)
        self.window_menu.add_command(label='Embedded Windows', command=self.generic_callback)
        self.menubar.add_cascade(label='Window', menu=self.window_menu, underline=0)

        self.parts_menu = tk.Menu(self.menubar, tearoff=0)
        self.parts_menu.add_command(label='Parts List 1', command=self.generic_callback)
        self.parts_menu.add_command(label='Parts List 2', command=self.generic_callback)
        self.parts_menu.add_command(label='Parts List 3', command=self.generic_callback)
        self.menubar.add_cascade(label='Parts', menu=self.parts_menu, underline=0)
        
        self.menubar.add_command(label='QuickFilter', command=self.quickfilter_callback)
        self.menubar.add_command(label='Advanced', command=self.advanced_callback)
        
        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label='Contents and Index', command=self.generic_callback)
        self.help_menu.add_command(label='PDF Help', command=self.generic_callback)
        self.help_videos_menu = tk.Menu(self.help_menu, tearoff=0)
        self.help_videos_menu.add_command(label='Bridged Element Delay Equalization', command=self.generic_callback)
        self.help_videos_menu.add_command(label='Efficient Design with Constricted Ripple', command=self.generic_callback)
        self.help_videos_menu.add_command(label='Schematic Edit Capabilities', command=self.generic_callback)
        self.help_videos_menu.add_command(label='Digital Synthesis and Simulations', command=self.generic_callback)
        self.help_videos_menu.add_command(label='Designing with Manufacturer\'s Parts', command=self.generic_callback)
        self.help_videos_menu.add_command(label='QuickFilter Overview', command=self.generic_callback)
        self.help_menu.add_cascade(label='Short Help Videos', menu=self.help_videos_menu, underline=0)
        self.folders_menu = tk.Menu(self.help_menu, tearoff=0)
        self.folders_menu.add_command(label='Program Directory', command=self.generic_callback)
        self.folders_menu.add_command(label='User\'s INI Directory', command=self.generic_callback)
        self.folders_menu.add_command(label='Documents Directory', command=self.generic_callback)
        self.help_menu.add_command(label='About...', command=self.generic_callback)
        self.menubar.add_cascade(label='Help', menu=self.help_menu, underline=0)
        
    def create_widgets(self):
        pass
        
    def generic_callback(self):
        pass
        
    def quickfilter_callback(self):
        self.show_form("QuickFilter")
    
    def advanced_callback(self):
        self.show_form("Advanced")

class NoticeWindow(tk.Toplevel):
    notice_text = """Dear Reader:

Thank you for your interest in NashHertz Filters.

NashHertz Filters has launched the QuickFilter panel to aid in
learning. QuickFilter is a user-friendly interface with a limited
subset of synthesis features.

   ***Select "Advanced" from the Main Menu***
to activate the main NashHertz Filters panel and to access full
synthesis power.

Several short Help videos are available in the Main Menu
"Help" section, including use with third parties, to introduce
advanced synthesis capabilities and to aid in learning.

Numerous project file examples are available under the Main
Menu "File" section.
"""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("QuickFilter User Notice")
        self.geometry("720x480")
        self.parent = parent
        
        self.display_booleanvar = tk.BooleanVar()
        
        self.notice_labelframe = tk.LabelFrame(self, text="NoticeBox")
        self.upper_frame = ttk.Frame(self.notice_labelframe)
        self.lower_frame = ttk.Frame(self.notice_labelframe)
        self.notice_text = tk.Text(self.upper_frame, height=25)
        self.close_button = tk.Button(self.lower_frame, text="Close", command=self.destroy)
        self.display_checkbutton = ttk.Checkbutton(self.lower_frame,
            text="Don't Show Me This Again",
            command=self.no_show,
            variable=self.display_booleanvar)
        
        self.notice_text.insert(index='1.0', chars=NoticeWindow.notice_text)
        
        self.notice_labelframe.pack()
        self.upper_frame.pack()
        self.lower_frame.pack()
        self.notice_text.pack()
        self.close_button.pack(side="left", padx=5)
        self.display_checkbutton.pack(side="left", padx=10)

    def no_show(self):
        pass
