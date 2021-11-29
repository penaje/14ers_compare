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
import webbrowser


def create_page_2():
    ssl._create_default_https_context = ssl._create_unverified_context

    def callback(url):
        webbrowser.open_new_tab(url)

    def clear_selection():
        """Clears the selected Peaks"""
        info.selected_peaks.clear()

    def load_page_1():
        """Renders Page 1"""
        clear_selection()
        page_2_top.withdraw()
        import page_1_grid
        page_1_grid.create_page_1()

    page_2_top = Toplevel()
    page_2_top.geometry('1400x900')
    page_2_top.title("Here's your information!")

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
    main_frame = Frame(page_2_top)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="#909C74")
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas, bg="#909C74")

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Create title labels
    title_1_label = Label(second_frame, text=info.peaks_title.get(info.selected_peaks[0]), font=('roboto', 20, 'bold'),
                          background="#909C74")
    title_1_label.grid(row=1, column=1, sticky=NW, padx=10, pady=5, ipadx=2, ipady=2)

    title_2_label = Label(second_frame, text=info.peaks_title.get(info.selected_peaks[1]), font=('roboto', 20, 'bold'),
                          background="#909C74")
    title_2_label.grid(row=1, column=4, sticky=NW, padx=10, pady=5, ipadx=2, ipady=2)

    # Create the Images
    img = img_from_url(url_list[0])  # Reference to image for the first peak user selected
    width_1 = img.width()
    height_1 = img.height()

    img_1_holder = Canvas(second_frame, width=width_1, height=height_1)
    img_1_holder.grid(row=1, rowspan=2, column=2, columnspan=2, padx=10, pady=5)
    img_1_holder.create_image(width_1, height_1, anchor=SE, image=img)

    img_2 = img_from_url(url_list[1])  # Reference to image for the second peak the user selected
    width_2 = img_2.width()
    height_2 = img_2.height()

    img_2_holder = Canvas(second_frame, width=width_2, height=height_2)
    img_2_holder.grid(row=1, rowspan=2, column=6, columnspan=2, padx=10, pady=5)
    img_2_holder.create_image(width_2, height_2, anchor=SE, image=img_2)

    # Create the info boxes
    info_box_1 = Frame(second_frame, padx=5, pady=5, bd=2, bg="#D3D3D3")
    info_box_1.grid(row=2, column=0, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)

    info_box_2 = Frame(second_frame, padx=5, pady=5, bd=2, bg="#D3D3D3")
    info_box_2.grid(row=2, column=4, columnspan=2, padx=10, pady=5, ipadx=2, ipady=2)

    # Create the info box information
    highest_point_1 = Label(info_box_1, text='Highest Point Info', font=('arial', 9, 'bold'), bg='#CBB191')
    highest_point_1.grid(row=0, column=0, columnspan=2, sticky=N)

    highest_point_2 = Label(info_box_2, text='Highest Point Info', font=('arial', 9, 'bold'), bg='#CBB191')
    highest_point_2.grid(row=0, column=0, columnspan=2, sticky=N)

    prominence_1 = Label(info_box_1, text="Prominence: " + info.peaks_prominence.get(info.selected_peaks[0]),
                         bg="#D3D3D3")
    prominence_1.grid(row=1, column=0, sticky=W)

    prominence_2 = Label(info_box_2, text="Prominence: " + info.peaks_prominence.get(info.selected_peaks[1]),
                         bg="#D3D3D3")
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

    coords_1 = Label(info_box_1, text="Coordinates: " + info.peaks_coord.get(info.selected_peaks[0]), bg="#D3D3D3")
    coords_1.grid(row=5, column=0, sticky=W)

    coords_2 = Label(info_box_2, text="Coordinates: " + info.peaks_coord.get(info.selected_peaks[1]), bg="#D3D3D3")
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

    # Create the clickable links
    link_1 = Label(second_frame, text=info.peaks_title.get(info.selected_peaks[0]) + ' on peakbagger.com',
                   font=('Helveticabold', 12), fg="blue", cursor="hand2", bg="#909C74")
    link_1.grid(row=5, column=2)
    link_1.bind("<Button-1>", lambda e: callback(info.peak_bagger_urls.get(info.selected_peaks[0])))

    link_2 = Label(second_frame, text=info.peaks_title.get(info.selected_peaks[1]) + ' on peakbagger.com',
                   font=('Helveticabold', 12), fg="blue", cursor="hand2", bg="#909C74")

    link_2.grid(row=5, column=6)
    link_2.bind("<Button-1>", lambda e: callback(info.peak_bagger_urls.get(info.selected_peaks[1])))

    # Create the style
    style = ttk.Style(second_frame)
    style.theme_names()
    style.theme_use('alt')

    # Create the buttons
    button_1_style = ttk.Style()
    button_1_style.configure('B1.TButton', font=('Arial', 10, 'bold'), foreground='black', background='#b2f7f4')
    button_1 = ttk.Button(second_frame, text='Back To Home!', command=lambda: load_page_1(), style='B1.TButton')

    button_1.grid(row=6, column=7)

    button_2_style = ttk.Style()
    button_2_style.configure('B2.TButton', font=('Arial', 10, 'bold'), foreground='black', background='#f06e6e')

    button_2 = ttk.Button(second_frame, text='Quit!', command=lambda: page_2_top.destroy(), style='B2.TButton')
    button_2.grid(row=6, column=1)

    # Create the map images

    # Image 1
    all_trail_img_1 = img_from_url(info.all_trails_maps.get(info.selected_peaks[0]))

    # Reference to image for the first peak user selected
    width_1 = all_trail_img_1.width()
    height_1 = all_trail_img_1.height()

    image_link_1 = Label(second_frame, image=all_trail_img_1, cursor="hand2")
    image_link_1.grid(row=3, rowspan=1, column=1, columnspan=1, padx=15, pady=10, ipadx=5, ipady=5)
    image_link_1.bind("<Button-1>", lambda e: callback(info.all_trails_links.get(info.selected_peaks[0])))

    # Image 2
    all_trail_img_2 = img_from_url(info.all_trails_maps.get(info.selected_peaks[1]))

    # Reference to image for the second peak user selected
    width_2 = all_trail_img_2.width()
    height_2 = all_trail_img_2.height()

    image_link_2 = Label(second_frame, image=all_trail_img_2, cursor="hand2")
    image_link_2.grid(row=3, rowspan=1, column=4, columnspan=1, padx=15, pady=10, ipadx=5, ipady=5)
    image_link_2.bind("<Button-1>", lambda e: callback(info.all_trails_links.get(info.selected_peaks[1])))

    page_2_top.mainloop()
