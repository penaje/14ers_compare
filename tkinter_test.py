# Testing out tkinter

import tkinter as tk

from tkinter import *

window = tk.Tk()

greeting = tk.Label(text="Hello World")

greeting.pack()

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.pack()

label.pack()

window.mainloop()
