
from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


selected_peaks = []

test_text = 'This is a test!'


def add_button_name_to_selection(peak_name):
    selected_peaks.append(peak_name)
    print(selected_peaks)


def clear_selection():
    selected_peaks.clear()


window = Tk()

window.geometry("1440x1024")
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
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Mt Whitney'),
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
    text="Please Select 2 - 3 Peaks to Compare",
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

button_image_2 = PhotoImage(
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

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
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

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1019.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1019.0,
    y=881.0,
    width=243.0,
    height=78.0001220703125
)

button_image_6 = PhotoImage(
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
    y=881.0,
    width=243.0,
    height=78.0001220703125
)

text_to_display = 'Mt Whitney, Mt Rainer'

w = Label(window, text='Here is your selected peaks:', font='48', fg='gray')
w.pack()

msg = Message(window, text=text_to_display)
msg.pack()

window.resizable(True, True)
window.mainloop()
