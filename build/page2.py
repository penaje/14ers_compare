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

ssl._create_default_https_context = ssl._create_unverified_context

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def clear_selection():
    info.selected_peaks.clear()


def load_page_1():
    clear_selection()
    window.destroy()
    import page1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

images = []


def img_from_url(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    images.append(image)


url_list = image_import.import_images(info.selected_peaks)

for url in url_list:
    img_from_url(url)

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
img = images[0]
width_1 = img.width()
height_1 = img.height()

img_1_holder = Canvas(canvas, width=width_1, height=height_1)
img_1_holder.place(x=400.0, y=32.0)
img_1_holder.create_image(width_1, height_1, anchor=SE, image=img)

img_2 = images[1]
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
    346.0,
    305.0,
    696.0,
    755.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    1072.0,
    305.0,
    1422.0,
    755.0,
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

canvas.create_text(  # Peak #1 Climbing Route
    362.0,
    340.0,
    anchor="nw",
    width=320,
    text=info.peaks_dict.get(info.selected_peaks[0]),
    fill="#000000",
    font=("Roboto", 18 * -1)
)

canvas.create_text(  # Peak 2 Climbing Route
    1088.0,
    340.0,
    anchor="nw",
    width=320,
    text=info.peaks_dict.get(info.selected_peaks[1]),
    fill="#000000",
    font=("Roboto", 18 * -1)
)
window.resizable(False, False)
window.mainloop()
