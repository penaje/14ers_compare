from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from urllib.request import urlopen
import urllib
import io
import info
import image_import
import ssl
from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tkst

ssl._create_default_https_context = ssl._create_unverified_context

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def clear_selection():
    """Clears the selected Peaks"""
    info.selected_peaks.clear()


def load_page_1():
    """Renders Page 1"""
    clear_selection()
    root.destroy()
    import page1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()
root.title("Here's your information!")
root.geometry("1400x900")
root.configure(bg="#FFFFFF")


def img_from_url(url):
    """Returns an Image object from a url string"""
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image


# Runs my import_images function from image_import.py on the peaks the user
# selected on Page_1
url_list = image_import.import_images(info.selected_peaks)

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
my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="#FFFFFF")
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Create title labels
title_1_label = Label(second_frame, text="Mt. Whitney", font=('roboto', 20, 'bold'))
title_1_label.grid(row=1, column=1, sticky=NW, padx=10, pady=5, ipadx=2, ipady=2)

title_2_label = Label(second_frame, text="Mt. Elbert", font=('roboto', 20, 'bold'))
title_2_label.grid(row=1, column=4, sticky=NW, padx=10, pady=5, ipadx=2, ipady=2)

# Create the Images
img = img_from_url(url_list[0])  # Reference to image for the first peak user selected
width_1 = img.width()
height_1 = img.height()

img_1_holder = Canvas(second_frame, width=width_1, height=height_1)
img_1_holder.grid(row=1, rowspan=2, column=2, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)
img_1_holder.create_image(width_1, height_1, anchor=SE, image=img)

img_2 = img_from_url(url_list[1])  # Reference to image for the second peak the user selected
width_2 = img_2.width()
height_2 = img_2.height()

img_2_holder = Canvas(second_frame, width=width_2, height=height_2)
img_2_holder.grid(row=1, rowspan=2, column=6, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)
img_2_holder.create_image(width_2, height_2, anchor=SE, image=img_2)

# Create the info boxes
info_box_1 = Frame(second_frame, padx=5, pady=5, bd=2, bg="#D3D3D3")
info_box_1.grid(row=2, column=0, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)

info_box_2 = Frame(second_frame, padx=5, pady=5, bd=2, bg="#D3D3D3")
info_box_2.grid(row=2, column=4, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)

# Create the info box information
highest_point_1 = Label(info_box_1, text='Highest Point', font=('arial', 10, 'bold'), bg='#CBB191')
highest_point_1.grid(row=0, column=0, columnspan=2, sticky=N)

highest_point_2 = Label(info_box_2, text='Highest Point', font=('arial', 10, 'bold'), bg='#CBB191')
highest_point_2.grid(row=0, column=0, columnspan=2, sticky=N)

prominence_1 = Label(info_box_1, text="Prominence: " + info.peaks_prominence.get(info.selected_peaks[0]), bg="#D3D3D3")
prominence_1.grid(row=1, column=0, sticky=W)

prominence_2 = Label(info_box_2, text="Prominence: " + info.peaks_prominence.get(info.selected_peaks[1]), bg="#D3D3D3")
prominence_2.grid(row=1, column=0, sticky=W)

elevation_1 = Label(info_box_1, text="Elevation: " + info.peaks_elevation.get(info.selected_peaks[0]), bg="#D3D3D3")
elevation_1.grid(row=2, column=0, sticky=W)

elevation_2 = Label(info_box_2, text="Elevation: " + info.peaks_elevation.get(info.selected_peaks[1]), bg="#D3D3D3")
elevation_2.grid(row=2, column=0, sticky=W)

isolation_1 = Label(info_box_1, text="Isolation: " + info.peaks_isolation.get(info.selected_peaks[0]), bg="#D3D3D3")
isolation_1.grid(row=3, column=0, sticky=W)

isolation_2 = Label(info_box_2, text="Isolation: " + info.peaks_isolation.get(info.selected_peaks[1]), bg="#D3D3D3")
isolation_2.grid(row=3, column=0, sticky=W)

state_1 = Label(info_box_1, text="State: " + info.peaks_state.get(info.selected_peaks[0]), bg="#D3D3D3")
state_1.grid(row=4, column=0, sticky=W)

state_2 = Label(info_box_2, text="State: " + info.peaks_state.get(info.selected_peaks[1]), bg="#D3D3D3")
state_2.grid(row=4, column=0, sticky=W)

coords_1 = Label(info_box_1, text="Coordinates: " + info.peaks_state.get(info.selected_peaks[0]), bg="#D3D3D3")
coords_1.grid(row=5, column=0, sticky=W)

coords_2 = Label(info_box_2, text="Coordinates: " + info.peaks_state.get(info.selected_peaks[1]), bg="#D3D3D3")
coords_2.grid(row=5, column=0, sticky=W)

# Create the text boxes
climbing_info_frame_1 = Frame(  # Holds the frame around the text box
    master=second_frame,
    bg='#000000',
    height=400,
    width=250
)
climbing_info_frame_1.grid(row=3, column=2, padx=10, pady=5, ipadx=2, ipady=2)

text_area = tkst.ScrolledText(  # Holds the text
    master=climbing_info_frame_1,
    wrap=tk.WORD,
    width=35,
    height=30,
    font=('arial', 8, 'bold')
)

text_area.pack(padx=5, pady=5, fill=BOTH, expand=True)
text_area.insert(tk.INSERT, info.peaks_dict.get(info.selected_peaks[0]))
text_area.configure(state='disabled')

climbing_info_frame_2 = Frame(  # Holds the frame around the text box
    master=second_frame,
    bg='#000000',
    height=400,
    width=250
)
climbing_info_frame_2.grid(row=3, column=6, padx=10, pady=5, ipadx=2, ipady=2)

text_area = tkst.ScrolledText(  # Holds the text
    master=climbing_info_frame_2,
    wrap=tk.WORD,
    width=35,
    height=30,
    font=('arial', 8, 'bold')
)

text_area.pack(padx=5, pady=5, fill=BOTH, expand=True)
text_area.insert(tk.INSERT, info.peaks_dict.get(info.selected_peaks[1]))
text_area.configure(state='disabled')

root.mainloop()