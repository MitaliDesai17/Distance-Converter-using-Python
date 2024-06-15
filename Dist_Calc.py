import tkinter as tk
import random

class Dist_calc:
    dict = {"km2m": 0.621371, "m2km": 1.60934, "m2y": 1.09361, "y2m": 0.9144}
    colour = ["Yellow","Blue","Green","Brown"]
    

    def __init__(self):
        Dist_calc.main_window = tk.Tk()
        Dist_calc.main_window.Title = ("Distance Converter")
        Dist_calc.entry_variable = tk.StringVar()
        Dist_calc.entry_variable.set("Enter a number")
        Dist_calc.make_widgets()
        Dist_calc.main_window.mainloop()

    def make_widgets():
        Dist_calc.entry = tk.Entry(Dist_calc.main_window, textvariable = Dist_calc.entry_variable)
        Dist_calc.entry.grid(row = 0, column = 0, columnspan = 4)
        Dist_calc.b1 = tk.Button(Dist_calc.main_window, text = "Kilometre to Miles", command = lambda : Dist_calc.callback("km2m") )
        Dist_calc.b1.grid(row = 1, column = 0)
        Dist_calc.b2 = tk.Button(Dist_calc.main_window, text = "Miles to Kilometre", command = lambda : Dist_calc.callback("m2km") )
        Dist_calc.b2.grid(row = 1, column = 1)
        Dist_calc.b3 = tk.Button(Dist_calc.main_window, text = "Miles to Yards", command = lambda : Dist_calc.callback("m2y") )
        Dist_calc.b3.grid(row = 1, column = 2)
        Dist_calc.b4 = tk.Button(Dist_calc.main_window, text = "Yards to Miles", command = lambda : Dist_calc.callback("y2m") )
        Dist_calc.b4.grid(row = 1, column = 3)

    def callback(cmd):
        num = Dist_calc.entry_variable.get()
        Dist_calc.main_window.configure(bg = random.choice(Dist_calc.colour))
        try:
            n = float(num)
            
            Dist_calc.entry_variable.set("{:7.3f}".format(round(n * Dist_calc.dict[cmd],3)))
        except:
            Dist_calc.entry_variable.set("Error!")

obj = Dist_calc()


