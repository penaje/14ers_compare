from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

import info  # Import the info file

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def load_page_2():
    """Renders page 2"""
    window.destroy()
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


window = Tk()
window.geometry("1440x800")
window.configure(bg="#FFFFFF")

# Create a Main Frame
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# Create a Canvas
canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview())
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Create another frame
second_frame = Frame(canvas)

# Add that new frame to a window in the canvas
canvas.create_window((0, 0), window=second_frame, anchor='nw')

whitney_button = Button(
    text="Mt. Whitney",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Whitney'),
    relief="flat"
)
whitney_button.place(
    x=89.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

shasta_button = Button(
    text='Mt.Shasta',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Shasta'),
    relief="flat"
)
shasta_button.place(
    x=89.0,
    y=395.0,
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

denali_button_image = PhotoImage(  # Denali
    file=relative_to_assets("button_2.png"))
denali_button = Button(
    image=denali_button_image,
    borderwidth=2,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Denali'),
    relief="flat"
)
denali_button.place(
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

elbert_button_image = PhotoImage(  # Mt Elbert
    file=relative_to_assets("button_3.png"))
elbert_button = Button(
    image=elbert_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Elbert'),
    relief="flat"
)
elbert_button.place(
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

rainier_button_image = PhotoImage(  # Mt Rainier
    file=relative_to_assets("button_4.png"))
rainier_button = Button(
    image=rainier_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_button_name_to_selection('Rainier'),
    relief="flat"
)
rainier_button.place(
    x=1019.0,
    y=295.0,
    width=243.0,
    height=78.0001220703125
)

submit_button_image = PhotoImage(  # Submit Button
    file=relative_to_assets("button_5.png"))
submit_button = Button(
    image=submit_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load_page_2(),
    relief="flat"
)
submit_button.place(
    x=1019.0,
    y=681.0,
    width=243.0,
    height=78.0001220703125
)

clear_button_image = PhotoImage(  # Clear Selection
    file=relative_to_assets("button_6.png"))
clear_button = Button(
    image=clear_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear_selection(),
    relief="flat"
)
clear_button.place(
    x=89.0,
    y=681.0,
    width=243.0,
    height=78.0001220703125
)

window.resizable(True, True)
window.mainloop()
