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
    window.destroy()
    import page1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Create an instance of tkinter
window = Tk()
window.geometry("1440x1000")
window.configure(bg="#FFFFFF")


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
img = img_from_url(url_list[0])  # Reference to image for the first peak user selected
width_1 = img.width()
height_1 = img.height()

img_1_holder = Canvas(canvas, width=width_1, height=height_1)
img_1_holder.place(x=400.0, y=32.0)
img_1_holder.create_image(width_1, height_1, anchor=SE, image=img)

img_2 = img_from_url(url_list[1])  # Reference to image for the second peak the user selected
width_2 = img_2.width()
height_2 = img_2.height()

img_2_holder = Canvas(canvas, width=width_2, height=height_2)
img_2_holder.place(x=1100, y=32.0)
img_2_holder.create_image(width_2, height_2, anchor=SE, image=img_2)

canvas.create_rectangle(
    38.0,
    32.0,
    300.0,
    88.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    764.0,
    32.0,
    1026.0,
    88.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    16.0,
    113.0,
    300.0,
    375.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    742.0,
    113.0,
    1026.0,
    375.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    38.0,
    936.0,
    229.0,
    984.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    764.0,
    936.0,
    955.0,
    984.0,
    fill="#C4C4C4",
    outline="")

style = ttk.Style(window)
style.theme_names()
style.theme_use('alt')

button_1_style = ttk.Style()
button_1_style.configure('B1.TButton', font=('Arial', 10, 'bold'), foreground='black', background='#b2f7f4')
button_1 = ttk.Button(window, text='Back To Home!', command=lambda: load_page_1(), style='B1.TButton')

button_1.place(
    x=1196.0,
    y=933.0,
    width=187.0,
    height=51.0
)

button_2_style = ttk.Style()
button_2_style.configure('B2.TButton', font=('Arial', 10, 'bold'), foreground='black', background='#f06e6e')

button_2 = ttk.Button(window, text='Quit!', command=lambda: window.destroy(), style='B2.TButton')
button_2.place(
    x=975.0,
    y=933.0,
    width=150.0,
    height=50.0
)

canvas.create_text(  # Title #1
    38.0,
    32.0,
    anchor="nw",
    text=info.peaks_title.get(info.selected_peaks[0]),
    fill="#000000",
    font=("Roboto", 36 * -1)
)

canvas.create_text(  # Title #2
    763.0,
    32.0,
    anchor="nw",
    text=info.peaks_title.get(info.selected_peaks[1]),
    fill="#000000",
    font=("Roboto", 36 * -1)
)

canvas.create_text(  # Elevation #1
    23.0,
    128.0,
    anchor="nw",
    text="Elevation:" + info.peaks_elevation.get(info.selected_peaks[0]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(  # Elevation #2
    754.0,
    128.0,
    anchor="nw",
    text="Elevation:" + info.peaks_elevation.get(info.selected_peaks[1]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(  # Prominence # 1
    22.0,
    152.0,
    anchor="nw",
    text="Prominence:" + info.peaks_prominence.get(info.selected_peaks[0]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(  # Prominence # 2
    753.0,
    152.0,
    anchor="nw",
    text="Prominence:" + info.peaks_prominence.get(info.selected_peaks[1]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(  # Isolation#1
    22.0,
    176.0,
    anchor="nw",
    text="Isolation:" + info.peaks_isolation.get(info.selected_peaks[0]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(  # Isolation#2
    753.0,
    176.0,
    anchor="nw",
    text="Isolation:" + info.peaks_isolation.get(info.selected_peaks[1]),
    fill="#000000",
    font=("Roboto", 12 * -1)
)

canvas.create_text(
    432.0,
    305.0,
    anchor="nw",
    text="Climbing Routes",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    1170.0,
    311.0,
    anchor="nw",
    text="Climbing Routes",
    fill="#000000",
    font=("Roboto", 24 * -1)
)

canvas.create_text(
    475,
    250,
    anchor='nw',
    text='Climbing Info',
    fill="#000000",
    font=('Roboto', 20 * -1)
)

canvas.create_text(
    1175,
    250,
    anchor='nw',
    text='Climbing Info',
    fill="#000000",
    font=('Roboto', 20 * -1)
)

climbing_info_frame_1 = tk.Frame(  # Holds the frame around the text box
    master=window,
    bg='#000000',
    height=400,
    width=250
)
climbing_info_frame_1.place(x=400, y=300)
text_area = tkst.ScrolledText(  # Holds the text
    master=climbing_info_frame_1,
    wrap=tk.WORD,
    width=30,
    height=30
)

text_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
text_area.insert(tk.INSERT, info.peaks_dict.get(info.selected_peaks[0]))
text_area.configure(state='disabled')

climbing_info_frame_2 = tk.Frame(  # Holds the frame around the text box
    master=window,
    bg='#000000',
    height=400,
    width=250
)
climbing_info_frame_2.place(x=1100, y=300)
text_area_2 = tkst.ScrolledText(  # Holds the text
    master=climbing_info_frame_2,
    wrap=tk.WORD,
    width=30,
    height=30
)

text_area_2.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
text_area_2.insert(tk.INSERT, info.peaks_dict.get(info.selected_peaks[1]))
text_area_2.configure(state='disabled')

window.resizable(True, True)
window.mainloop()
