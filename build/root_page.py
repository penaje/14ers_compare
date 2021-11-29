from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter.ttk import *
import info  # Import the info file
import page_1_grid

root = Tk()
root.withdraw()

page_1_grid.create_page_1()

root.mainloop()
