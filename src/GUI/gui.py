import os
import copy
import threading
import tkinter as tk
from time import sleep

from Maze.maze import Maze
from Maze.solver import Solver
from GUI.settings import Settings

# This instantiates a window as the class object GUI
class GUI(tk.Tk):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Change title of the window
        self.title("Maze Solver")
        # Change initial size of window to 1000px by 1000px
        self.geometry("1000x1000")
        # Change icon of program to custom ico file
        icon_path = os.path.join(os.path.dirname(__file__), "../Assets/Backrooms_model.ico")
        icon_path = os.path.abspath(icon_path)
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except tk.TclError:
                print(f"Warning: Unable to load icon: {icon_path}")

        self.stack = [] # Create empty array to be used as a stack
        # Create empty array to be used as the directions towards the exit
        self.path = []
        # Create boolean which changes whist the maze is being solved
        self.is_solving = False

        # Create instance of Canvas class
        self.canvas = tk.Canvas(self, bg="#313639")
        # Pack canvas onto the Tk window
        self.canvas.pack(fill="both", expand=True)
        # Create instance of Solver class
        self.solving = Solver()
        # Create instance of Maze class
        self.maze = Maze(15, 15)
        # Create instance of Settings class
        self.settings_menu = Settings(self.canvas, command=self.thread, bg="#313639")

        # Set coordinates for the start point of the maze
        self.start_point = (0, 0)
        # Set the coodinates for the end point of the maze
        self.end_point = (len(self.maze.maze[0]) - 1, len(self.maze.maze) - 1)
        
        # Calls the resize function when the size of the canvas changes
        self.bind("<Configure>", self.resize)
        # Bind 'escape' to open/close main menu
        self.bind("<Escape>", self.menu_handler)
        # Bind 'c' to clear the path displayed between start and end point
        self.bind("<c>", self.settings_menu.center_frame.clear_path)
        # Bind 'C' to clear the path displayed between start and end point
        self.bind("<C>", self.settings_menu.center_frame.clear_path)
        # Bind 'r' to generate a new random maze with the settings selected 
        self.bind("<r>", self.settings_menu.center_frame.new_maze)
        # Bind 'R' to generate a new random maze with the settings selected 
        self.bind("<R>", self.settings_menu.center_frame.new_maze)
        # Bind 'x' to solve the maze
        self.bind("<x>", self.thread)
        # Bind 'X' to solve the maze
        self.bind("<X>", self.thread)
        # Bind 'right arrow' to increase the width of the maze
        self.bind("<Right>", self.settings_menu.left_frame.plus_width)
        # Bind 'left arrow' to decrease the width of the maze
        self.bind("<Left>", self.settings_menu.left_frame.minus_width)
        # Bind 'up arrow' to increase the height of the maze
        self.bind("<Up>", self.settings_menu.left_frame.plus_height)
        # Bind 'down arrow' to decrease the height of the maze
        self.bind("<Down>", self.settings_menu.left_frame.minus_height)
        

    # Using a stack in order to open and close the settings menu
    def menu_handler(self, event=None):
        self.stack = list(set(self.stack))
        if len(self.stack) == 0:
            self.stack.append(self.settings_menu)
            self.settings_menu.place(relx=0, rely=0)

        else:
            self.stack[-1].place_forget()
            self.stack.pop()

    #Updates the scale of the maze depending on the 
    def resize(self, event=None):
        self.settings_menu.config(width=self.winfo_width())
        self.maze.update_scale(self.winfo_width(), self.winfo_height())  

    # Generates the path towards solving the maze
    def create_path(self):
        path = self.solving.solve(self.maze.maze)
        path = [[y * -1, x * -1] for y, x in path]
        coord = [0, 0]

        for i in path:
            coord[0] += i[0]
            coord[1] += i[1]
            self.path.append(copy.deepcopy(coord))
            sleep(0.1)
        self.is_solving = False

    # Using a thread when the path is starting to be displayed
    def thread(self, event=None):
        if not self.path:
            self.is_solving = True
            threading.Thread(target=self.create_path).start()

    # Draw path function used for drawing the path
    def draw_path(self):
        if not self.path:
            return
        gradient = 100/len(self.path)
        for i, v in enumerate(self.path):
            self.maze.draw_square(self.canvas, *v[::-1], f"#00{hex(int(i*gradient)+155)[2:].zfill(2)}00")


if __name__ == "__main__":
    root = GUI()
    root.run()
