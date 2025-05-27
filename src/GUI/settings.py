import tkinter as tk
from GUI import LeftFrame, CenterFrame, RightFrame

class Settings(tk.Canvas):
    def __init__(self, *args, command=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.root = self.master.master # accesses the main instance of Tk 

        # create instance of the CenterFrame class
        self.center_frame = CenterFrame(self, bg="#313639", command=command)
        self.center_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # create instance of the LeftFrame class
        self.left_frame = LeftFrame(self, bg="#313639", command=command)
        self.left_frame.place(relx=0.15, rely=0.5, anchor=tk.W)

        # create instance of the RightFrame class
        self.right_frame = RightFrame(self, bg="#202528", command=command)
        self.right_frame.place(relx=0.85, rely=0.5, anchor=tk.E)

        # create button that will close the settings menu
        self.exit_button = tk.Button(self, text="X", command=self.root.menu_handler)
        self.exit_button.place(relx=1, rely=0, anchor=tk.NE)
