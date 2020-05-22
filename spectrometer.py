import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk
from tkinter import *

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

class Spectrometer(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="") # set icon 16x16
        tk.Tk.wm_title(self, "Spectrometer Client") # set title

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row = 0, column = 0, sticky="nsew")
        
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame= self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Spectrometer", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
          

        #button1 = ttk.Button(self, text="Agree", command=lambda:  controller.show_frame(BTCe_page) )
        #button1.pack()



app= Spectrometer()
app.mainloop()
