import tkinter as tk
from Maze.maze import Maze

class CenterFrame(tk.Frame):
    def __init__(self, *args, command=None, **kwargs):
        super().__init__(*args, **kwargs)
        # accesses the main instance of Tk
        self.root = self.master.master.master 

        # create button that accesses the create_path function
        self.solve_button = tk.Button(
            self,
            text="Solve",
            bg="#202528",
            fg="white",
            width=4,
            height=2,
            command=command,
        )

        # create button that accesses the clear_path function
        self.clear_path_button = tk.Button(
            self,
            text="Clear",
            bg="#202528",
            fg="white",
            width=4,
            height=2,
            command=self.clear_path,
        )

        # create button that accesses the new_maze function
        self.regenerate_button = tk.Button(
            self,
            text="Regenerate",
            bg="#202528",
            fg="white",
            width=9,
            height=2,
            command=self.new_maze,
        )

        self.solve_button.grid(row=0, column=0)
        self.clear_path_button.grid(row=0, column=1)
        self.regenerate_button.grid(row=0, column=2)

    # clear path that shows how to solve the maze
    def clear_path(self, event=None):
        if not self.root.is_solving:
            self.root.path = []

    def new_maze(self, event=None):
        """
        Function that clears the maze's path and then creates a new 
        random maze with the selected witdth and height values
        """
        # check if the maze is in the middle of displaying the path
        if not self.root.is_solving:
            self.root.path = [] # set path to empty array
            # set new end-point for the maze depending on its width and height
            self.root.end_point = (
                round(self.master.left_frame.height_slider.get()) - 1,
                round(self.master.left_frame.width_slider.get()) - 1,
            )
            # create new maze depending on the width and height of sliders
            self.root.maze = Maze(
                round(self.master.left_frame.width_slider.get()),
                round(self.master.left_frame.height_slider.get()),
            )
            # update the scale of the maze based on window's width and height
            self.root.maze.update_scale(
                self.root.winfo_width(), self.root.winfo_height()
            )

