import tkinter as tk

class RightFrame(tk.Frame):
    def __init__(self, *args, command=None, **kargs):
        super().__init__(*args, **kargs)
        # Label that states how to access the menu pop-up through keybind
        self.toggle_menu_command = tk.Label(
            self,
            text="Toggle Menu: ESC",
            bg="#202528",
            fg="white")
        # Label that states how to access the solve function through keybind
        self.solve_command = tk.Label(
            self,
            text="Solve Maze: X",
            bg="#202528",
            fg="white",
        )
        # Label that states how to access the clear function through keybind
        self.clear_command = tk.Label(
            self,
            text="Clear path: C",
            bg="#202528",
            fg="white",
        )
        # Label that shows how to access the new maze function through keybind
        self.new_maze_command = tk.Label(
            self,
            text="Generate new maze: R",
            bg="#202528",
            fg="white",
        )
        # Label that shows how to access the plus width function with keybind
        self.plus_width_command = tk.Label(
            self,
            text="Increase Width: UpArrow",
            bg="#202528",
            fg="white",
        )
        # Label that shows how to access the minus width function with keybind
        self.minus_width_command = tk.Label(
            self,
            text="Decrease Width: DownArrow",
            bg="#202528",
            fg="white",
        )
        # Label that shows how to access the plus height function with keybind
        self.plus_height_command = tk.Label(
            self,
            text="Increase Height: Right Arrow",
            bg="#202528",
            fg="white",
        )
        # Label showing how to access the minus height function with keybind
        self.minus_height_command = tk.Label(
            self,
            text="Decrease Height: Left Arrow",
            bg="#202528",
            fg="white",
        )

        # Putting all the labels into a grid on the left hand side of the GUI
        self.toggle_menu_command.grid(row=0, column=0)
        self.solve_command.grid(row=1, column=0)
        self.clear_command.grid(row=2, column=0)
        self.new_maze_command.grid(row=3, column=0)
        self.plus_width_command.grid(row=4, column=0)
        self.minus_width_command.grid(row=5, column=0)
        self.plus_height_command.grid(row=6, column=0)
        self.minus_height_command.grid(row=7, column=0)

