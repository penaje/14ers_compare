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

ssl._create_default_https_context = ssl._create_unverified_context

url_one = 'https:' + image_import.import_images()[0]
url_two = 'https:' + image_import.import_images()[1]

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def img_from_url(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image


def clear_selection():
    info.selected_peaks.clear()


def load_page_1():
    clear_selection()
    window.destroy()
    import page1


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg="#FFFFFF")

image_one = img_from_url(url_two)
width = image_one.width()
height = image_one.height()

print(height, width)

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

img_1_holder = Canvas(canvas, width=200, height=200)
img_1_holder.place(x=419.0, y=32.0)

img = img_from_url(url_one)  # NEW
img_1_holder.create_image(200, 200, anchor=SE, image=img)

img_2_holder = Canvas(canvas, width=200, height=200)
img_2_holder.place(x=1162, y=32.0)

img_2 = img_from_url(url_two)  # NEW
img_2_holder.create_image(200, 200, anchor=SE, image=img_2)

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

button_image_1 = PhotoImage(  # Back to home button
    file=relative_to_assets("button_1_pg_2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: load_page_1(),
    relief="flat"
)
button_1.place(
    x=1196.0,
    y=933.0,
    width=187.0,
    height=51.0
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
