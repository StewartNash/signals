import tkinter as tk
from tkinter import ttk

import math

class TableView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columns = ("Requirements", "Value", "Unit")

        self.tree = ttk.Treeview(
            self,
            columns=self.columns,
            show="headings",
            selectmode="browse"
        )

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)
        self.tree.column("Value", width=80)
        self.tree.tag_configure("odd", background="#f4f4f4")
        self.tree.tag_configure("even", background="#ffffff")

        # Sample data
        data = [
            ("Passband Attenuation", 30, "dB"),
            ("Stopband Attenuation", 40, "dB"),
            ("Impedance", 50, "Ohms"),
            ("Inductor Q", float('inf'), ""),
            ("Capacitor Q", float('inf'), "")
        ]
        
        #for row in data:
        #    self.tree.insert("", tk.END, values=row)
        for i, row in enumerate(data):
            tag = "even" if i % 2 == 0 else "odd"
            self.tree.insert("", tk.END, values=row, tags=(tag,))

        # Scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Bind editing events
        self.tree.bind("<Double-1>", self._begin_edit)

        self.editor = None
        self.unit_editor = ttk.Combobox(
            self,
            values=("dB", "Hz", "Ohms", "None"),
            state="readonly"
        )
        self.unit_editor.place_forget()


    # -----------------------------
    # Cell Editing
    # -----------------------------
    def _begin_edit(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region != "cell":
            return

        row_id = self.tree.identify_row(event.y)
        column = self.tree.identify_column(event.x)

        if not row_id or not column:
            return
            
        if column == "#3":
            x, y, width, height = self.tree.bbox(row_id, column)

            current_value = self.tree.set(row_id, "Unit")
            self.unit_editor.set(current_value)

            self.unit_editor.place(
                x=x,
                y=y,
                width=width,
                height=height
            )

            self.unit_editor.focus()
            self.editing_row = row_id

            def save_unit(event=None):
                new_value = self.unit_editor.get()
                self.tree.set(self.editing_row, "Unit", new_value)
                self.unit_editor.place_forget()
            
            self.unit_editor.bind("<<ComboboxSelected>>", save_unit)
            self.unit_editor.bind("<FocusOut>", save_unit)
        else:
            col_index = int(column[1:]) - 1
            x, y, width, height = self.tree.bbox(row_id, column)

            value = self.tree.item(row_id, "values")[col_index]

            # Create editor
            self.editor = ttk.Entry(self.tree)
            self.editor.insert(0, value)
            self.editor.select_range(0, tk.END)
            self.editor.focus()

            self.editor.place(x=x, y=y, width=width, height=height)

            def save_edit(event=None):
                new_value = self.editor.get()
                values = list(self.tree.item(row_id, "values"))
                values[col_index] = new_value
                self.tree.item(row_id, values=values)
                self.editor.destroy()
                self.editor = None

            def cancel_edit(event=None):
                self.editor.destroy()
                self.editor = None

            self.editor.bind("<Return>", save_edit)
            self.editor.bind("<FocusOut>", save_edit)
            self.editor.bind("<Escape>", cancel_edit)

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
        
        self.canvas_width = 400
        self.canvas_height = 300
        self.canvas_background = "black" #"white"
        
        self.is_grid_on = True
        
        self.line_color = "white"
        self.line_width = 3
        
        self.label_number = 0
        self.label_family = "Arial"
        self.label_font = 12
        self.label_style = "bold"
        
        self.grid_color = "gray"
        self.grid_vertical_lines = 10
        self.grid_horizontal_lines = 10
        self.grid_family = "Arial"
        self.grid_font = 10
        
        self.maximum_x = None
        self.minimum_x = None
        self.maximum_y = None
        self.minimum_y = None
        
        self.plots = []
        
        self.canvas = tk.Canvas(self,
            width=self.canvas_width,
            heigh=self.canvas_height,
            bg=self.canvas_background)
        self.canvas.pack()
        
        #step_size = 0.01
        #x = [i * step_size for i in range(0, int(2 * math.pi / step_size))]
        #y = [math.sin(x_) for x_ in x]        
        #self.plot(x, y, label="sin(x)")
        
    def clear(self, is_redrawing=False):
        self.canvas.delete("all")
        if is_redrawing:
            pass
        else:
            self.line_color = "white"
            self.line_width = 3
            
            self.label_number = 0
            self.label_family = "Arial"
            self.label_font = 12
            self.label_style = "bold"
            
            self.grid_color = "gray"
            self.grid_vertical_lines = 10
            self.grid_horizontal_lines = 10
            self.grid_family = "Arial"
            self.grid_font = 10
            
            self.maximum_x = None
            self.minimum_x = None
            self.maximum_y = None
            self.minimum_y = None
            
            self.plots = []
            
    def draw_grid(self):
        delta_x = self.canvas_width / self.grid_vertical_lines
        delta_y = self.canvas_height / self.grid_horizontal_lines
        
        maximum_x = self.maximum_x
        maximum_y = self.maximum_y
        minimum_x = self.minimum_x
        minimum_y = self.minimum_y
        
        inverse_transform_x = lambda x, max_x, min_x, width: (max_x - min_x) * (x - 0) / (width - 0) + min_x
        inverse_transform_y = lambda y, max_y, min_y, height: height - (max_y - min_y) * (y - height) / (height - 0) + min_y
        transform_x = lambda x, max_x, min_x, width: (width - 0) * (x - min_x) / (max_x - min_x) + 0
        transform_y = lambda y, max_y, min_y, height: height - (height - 0) * (y - min_y) / (max_y - min_y)
        
        # Draw and label vertical grid lines
        for i in range(self.grid_vertical_lines + 1):
            x = i * delta_x
            self.canvas.create_line(x, 0, x, self.canvas_height, fill=self.grid_color, dash=(2, 2))
            self.canvas.create_text(x, self.canvas_height - 10,
                text =f"{inverse_transform_x(x, maximum_x, minimum_x, self.canvas_width):.1f}",
                fill=self.grid_color,
                font=(self.grid_family, self.grid_font))

        # Draw and label horizontal grid lines
        for i in range(self.grid_horizontal_lines + 1):
            y = i * delta_y
            self.canvas.create_line(0, y, self.canvas_width, y, fill=self.grid_color, dash=(2, 2))
            self.canvas.create_text(10, y,
                text =f"{inverse_transform_y(y, maximum_y, minimum_y, self.canvas_height):.1f}",
                fill=self.grid_color,
                font=(self.grid_family, self.grid_font))
                
    def plot(self, x, y, label=None, color=None, is_redrawing=False):
        if not is_redrawing:
            maximum_x = max(x)
            maximum_y = max(y)
            minimum_x = min(x)
            minimum_y = min(y)
            is_redrawn = False
            #if self.maximum_x is None:
            if any(item is None for item in (self.maximum_x,
                self.maximum_y,
                self.minimum_x,
                self.minimum_y)):
                self.maximum_x = maximum_x
                self.maximum_y = maximum_y
                self.minimum_x = minimum_x
                self.minimum_y = minimum_y
                
                if self.is_grid_on:
                    self.draw_grid()
            else:
                is_bigger = False
                if maximum_x > self.maximum_x:
                    is_bigger = True
                    self.maximum_x = maximum_x
                elif maximum_y > self.maximum_y:
                    is_bigger = True
                    self.maximum_y = maximum_y
                elif minimum_x < self.minimum_x:
                    is_bigger = True
                    self.minimum_x = minimum_x
                elif minimum_y < self.minimum_y:
                    is_bigger = True
                    self.minimum_y = minimum_y
                    
                if is_beigger:
                    self.redraw()
            self.plots.append((x, y, label, color))
            
        maximum_x = self.maximum_x
        maximum_y = self.maximum_y
        minimum_x = self.minimum_x
        minimum_y = self.minimum_y
        
        if color:
            self.line_color = color
            
        #normalized_x = (x - minimum_x) / (maximum_x - minimum_x)
        #normalized_y = (y - minimum_y) / (maximum_y - minimum_y)
        #scaled_x = normalized_x * (self.canvas_width - 0) + 0 # 0 represents the minimum canvas x
        #scaled_y = height - normalized_y * (self.canvas_height - 0)
        
        normalized_x = [(x_ - minimum_x) / (maximum_x - minimum_x) for x_ in x]
        normalized_y = [(y_ - minimum_y) / (maximum_y - minimum_y) for y_ in y]
        scaled_x = [x_ * (self.canvas_width - 0) + 0 for x_ in normalized_x] # 0 represents the minimum canvas x
        scaled_y = [self.canvas_height - y_ * (self.canvas_height - 0) for y_ in normalized_y]
        x = scaled_x
        y = scaled_y
        
        for i in range(len(x) - 1):
            x1 = x[i]
            x2 = x[i + 1]
            y1 = y[i]
            y2 = y[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill=self.line_color, width=self.line_width)
            
        if label:
            self.canvas.create_text(
                3 * self.canvas_width / 4, 10 * (1 + self.label_number), # Top right
                text=label,
                fill=self.line_color,
                font=(self.label_family, self.label_font, self.label_style)
            )
            self.label_number = self.label_number + 1
            
    def redraw(self):
        self.clear(is_redrawing=True)
        if self.is_grid_on:
            self.draw_grid()
        for plot_ in self.plots:
            x = plot_[0]
            y = plot_[1]
            label = plot_[2]
            color = plot_[3]
            self.plot(x, y, label=label, color=color, is_redrawing=True)
       
