import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import(
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

def on_click():

    x, y = np.loadtxt('lampada.txt', delimiter = '/', unpack=True)
    time = datetime.now()
    txtTime = time.strftime('%d/%m/%Y %H:%M')
    title = "Sample - " + txtTime
    plt.title(title)
    plt.plot(x, y)
    plt.show()
    
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

        f = Figure(figsize = (5,5), dpi = 100)
        a = f.add_subplot(111)

        x = []
        y = []
    
        a.set_xlim(200, 850)
        a.set_ylim(0, 40000)
        
        plt.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button1 = ttk.Button(self, text="Acquire", command = on_click)
        button1.pack()






app= Spectrometer()
#app.configure(background='grey')
app.mainloop()
