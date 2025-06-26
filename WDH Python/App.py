import tkinter as tk
from tkinter import ttk
from components import Input
from util.functions import center_window
from style import init_style
import os, sys


class App(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)

        self.width = 800
        self.height = 400
        self.geometry(f"{self.width}x{self.height}")

        self.root_path = self.get_root_path()

        # Inputframe
        self.input_frame = Input(self)
        self.input_frame.pack(fill="both", expand=True)

        init_style()


    def get_root_path(self):
        path_to_main = os.path.abspath(sys.modules["__main__"].__file__)
        root_dir = os.path.dirname(path_to_main)
        return root_dir

    def run(self):
        center_window(self, self.width, self.height)

        self.mainloop()