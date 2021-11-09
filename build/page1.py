from pathlib import Path

from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import subprocess
import sys

import info  # Import the info file



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def load_page_2():
    window.destroy()
    import page2


def print_selection():
    print("Your selected Peaks are:")
    for item in info.selected_peaks:
        print(item)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_button_name_to_selection(peak_name):
    if len(info.selected_peaks) < 2:
        info.selected_peaks.append(peak_name)
        print(peak_name + " added to selection!")
        if len(info.selected_peaks) >= 1:
            print_selection()
    else:
        print("Two Peaks already selected, clear selection and retry!")


def clear_selection():
    info.selected_peaks.clear()


window = Tk()

window.geometry("1440x800")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

button_image_1 = PhotoImage(        # Mt Whitney
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Whitney'),
    relief="flat"
)
button_1.place(
    x=89.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

canvas.create_text(
    448.0,
    150.0,
    anchor="nw",
    text="Please Select 2 Peaks to Compare their Statistics!",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    86.0,
    230.0,
    anchor="nw",
    text="California",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    434.0,
    238.0,
    anchor="nw",
    text="Alaska",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

button_image_2 = PhotoImage(  # Denali
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=2,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Denali'),
    relief="flat"
)
button_2.place(
    x=399.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

canvas.create_rectangle(
    403.0,
    64.0,
    952.0,
    150.0,
    fill="#90F8FF",
    outline="")

canvas.create_text(
    441.0,
    76.0,
    anchor="nw",
    text="14er Comparison Tool",
    fill="#000000",
    font=("Roboto", 48 * -1)
)

canvas.create_text(
    729.0,
    238.0,
    anchor="nw",
    text="Colorado",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

button_image_3 = PhotoImage(  # Mt Elbert
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Elbert'),
    relief="flat"
)
button_3.place(
    x=709.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

canvas.create_text(
    1034.0,
    244.0,
    anchor="nw",
    text="Washington",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

button_image_4 = PhotoImage(  # Mt Rainier
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Rainier'),
    relief="flat"
)
button_4.place(
    x=1019.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

button_image_5 = PhotoImage(  # Submit Button
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load_page_2(),
    relief="flat"
)
button_5.place(
    x=1019.0,
    y=681.0,
    width=243.0,
    height=78.0001220703125
)

button_image_6 = PhotoImage(  # Clear Selection
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_selection(),
    relief="flat"
)
button_6.place(
    x=89.0,
    y=681.0,
    width=243.0,
    height=78.0001220703125
)

window.resizable(True, True)
window.mainloop()
