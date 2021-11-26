from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

import info  # Import the info file

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def load_page_2():
    """Renders page 2"""
    root.destroy()
    import page2


def print_selection():
    """Prints out what peaks were selected"""
    print("Your selected Peaks are:")
    for item in info.selected_peaks:
        print(item)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_button_name_to_selection(peak_name):
    """Prints out what selection was added"""
    if len(info.selected_peaks) < 2:
        info.selected_peaks.append(peak_name)
        print(peak_name + " added to selection!")
        if len(info.selected_peaks) >= 1:
            print_selection()
    else:
        print("Two Peaks already selected, clear selection and retry!")


def clear_selection():
    """Clears the user selection"""
    info.selected_peaks.clear()


root = Tk()
root.title('This is a test')
root.geometry("500x400")

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

title_label = Label(second_frame, text='14er Comparison Tool!')
title_label.grid(row=0, column=0)

selection_label = Label(second_frame, text='Please select two to three peaks to compare!')

root.mainloop()
