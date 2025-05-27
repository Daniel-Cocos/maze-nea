import tkinter as tk
from tkinter import ttk

class LeftFrame(tk.Frame):
    def __init__(self, *args, command=None, **kwargs):
        super().__init__(*args, **kwargs)
        # access the main instance of Tk
        self.root = self.master.master.master 

        # Slider that affects the width of the maze
        self.width_slider = ttk.Scale(
            self, from_=5, to=25, orient="horizontal", value=15, command=self.update_size
        )

        # Text that matches the value of the width slider
        self.width_slider_text = tk.Label(
            self,
            text=f"Width: {round(self.width_slider.get())}",
            bg="#313639",
            fg="white",
        )
    
        # Slider that affects the height of the maze
        self.height_slider = ttk.Scale(
            self, from_=5, to=25, orient="horizontal", value=15, command=self.update_size
        )

        # Text that matches the value of the height slider
        self.height_slider_text = tk.Label(
            self,
            text=f"Height: {round(self.height_slider.get())}",
            bg="#313639",
            fg="white",
        )

        # using grid to place the sliders and their labels for scaling purpose
        self.width_slider.grid(row=2, column=0)
        self.height_slider.grid(row=4, column=0)
        self.width_slider_text.grid(row=2, column=1)
        self.height_slider_text.grid(row=4, column=1)
    
    # fucntion that updates the text's values as sliders get moved
    def update_size(self, event=None):
        self.width_slider_text.config(text=f"Width: {round(self.width_slider.get())}")
        self.height_slider_text.config(text=f"Height: {round(self.height_slider.get())}")

    # function that increases the width by one
    def plus_width(self, event=None):
        self.width_slider.set(self.width_slider.get() + 1)

    # function that decreases the width by one
    def minus_width(self, event=None):
        self.width_slider.set(self.width_slider.get() - 1)

    # function that increases the height by one
    def plus_height(self, event=None):
        self.height_slider.set(self.height_slider.get() + 1)

    # function that decreases the height by one
    def minus_height(self, event=None):
        self.height_slider.set(self.height_slider.get() - 1)

