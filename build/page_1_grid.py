from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter.ttk import *
import info  # Import the info file
import page_2_grid
import page_3_grid
import tkinter as tk
import tkinter.ttk as ttk


def create_page_1():
    page_1_top = Toplevel()
    page_1_top.geometry('800x900')
    page_1_top.title("Select you peaks!")

    def load_page_2():
        """Renders page 2"""
        page_1_top.withdraw()
        page_2_grid.create_page_2()

    def load_page_3():
        """Renders page 3"""
        page_1_top.withdraw()
        page_3_grid.create_page_3()

    def load_selection():
        """Loads either page 2 or 3"""
        if len(info.selected_peaks) == 3:
            load_page_3()
        else:
            load_page_2()

    def print_selection():
        """Prints out what peaks were selected"""
        print("Your selected Peaks are:")
        for item in info.selected_peaks:
            print(item)

    def add_button_name_to_selection(peak_name):
        """Prints out what selection was added"""
        if len(info.selected_peaks) < 3:
            info.selected_peaks.append(peak_name)
            print(peak_name + " added to selection!")
            if len(info.selected_peaks) >= 1:
                print_selection()
        else:
            print("Three Peaks already selected, clear selection and retry!")

    # Add Peaks function
    def print_peaks():
        string_1 = ' & '.join([str(info.peaks_title.get(elem)) for elem in info.selected_peaks])
        selected_peaks_label_input.configure(text=string_1, background="#716352")

    # Call two functions for the buttons
    def add_and_print(peak_name):
        add_button_name_to_selection(peak_name)
        print_peaks()

    def clear_selection():
        """Clears the user selection"""
        info.selected_peaks.clear()
        selected_peaks_label_input.configure(text='', background="#716352")

    # Create A Main Frame
    main_frame = tk.Frame(page_1_top)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set, bg="#716352")
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = tk.Frame(my_canvas, bg="#716352")

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    # Add Styles
    style = ttk.Style(page_1_top)
    style.theme_use('clam')
    style.configure('peak.TButton', font=('calibri', 10, 'bold'), foreground='black', background="#886eab")
    style.configure('clear.TButton', font=('calibri', 10, 'bold'), foreground='black', background='#FF7276')
    style.configure('submit.TButton', font=('calibri', 10, 'bold'), foreground='black', background="#8A9A5B")

    style.map('peak.TButton', background=[('pressed', 'blue'),
                                          ('active', '#add8e6')])
    # Add Labels
    title_label = Label(second_frame, text='14er Comparison Tool!', font=('roboto', 20, 'bold'), foreground="#152238",
                        background="#716352")

    title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=2, ipadx=3, ipady=3)

    selection_label = Label(second_frame, text='Please select two to three peaks to compare!',
                            font=('calibri', 14, 'bold'), background="#716352", foreground="#1c2e4a"
                            )

    selection_label.grid(row=1, column=1, columnspan=5, padx=5, pady=2, ipadx=3, ipady=3)

    selected_peaks_label_title = Label(second_frame, text='Your selected peaks are:', font=('arial', 14, 'italic'),
                                       background="#716352")
    selected_peaks_label_title.grid(row=2, column=1, columnspan=3)

    selected_peaks_label_input = Label(second_frame, font=('arial', 12, 'bold'))
    selected_peaks_label_input.grid(row=2, column=4, columnspan=2)

    california_label = Label(second_frame, text='California',
                             font=('calibri', 14, 'bold'), background="#716352")

    california_label.grid(row=3, column=2, padx=10, pady=2, ipadx=3, ipady=3)

    alaska_washington_label = Label(second_frame, text='Alaska/Washington',
                                    font=('calibri', 14, 'bold'), background="#716352")

    alaska_washington_label.grid(row=3, column=3, padx=10, pady=2, ipadx=3, ipady=3)

    colorado_label = Label(second_frame, text='Colorado',
                           font=('calibri', 14, 'bold'), background="#716352")

    colorado_label.grid(row=3, column=4, padx=10, pady=2, ipadx=3, ipady=3)

    colorado_2_label = Label(second_frame, text='Colorado',
                             font=('calibri', 14, 'bold'), background="#716352")

    colorado_2_label.grid(row=3, column=5, padx=10, pady=2, ipadx=3, ipady=3)

    colorado_3_label = Label(second_frame, text='Colorado',
                             font=('calibri', 14, 'bold'), background="#716352")

    colorado_3_label.grid(row=3, column=6, padx=10, pady=2, ipadx=3, ipady=3)

    # Add  California buttons ; California column = 2
    whitney_button = Button(second_frame,
                            text="Mt. Whitney",
                            command=lambda: add_and_print('Whitney'),
                            style="peak.TButton"
                            )

    whitney_button.grid(row=4, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    shasta_button = Button(second_frame,
                           text='Mt. Shasta',
                           command=lambda: add_and_print('Shasta'),
                           style="peak.TButton"
                           )

    shasta_button.grid(row=5, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    white_button = Button(second_frame,
                          text='White Mt.',
                          command=lambda: add_and_print('White_Mountain'),
                          style="peak.TButton"
                          )

    white_button.grid(row=6, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    russell_button = Button(second_frame,
                            text='Mt. Russell',
                            command=lambda: add_and_print('Russell'),
                            style="peak.TButton"
                            )

    russell_button.grid(row=7, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    split_button = Button(second_frame,
                          text='Split Mt.',
                          command=lambda: add_and_print('Split'),
                          style="peak.TButton"
                          )

    split_button.grid(row=8, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    langley_button = Button(second_frame,
                            text='Mt. Langley',
                            command=lambda: add_and_print('Langley'),
                            style="peak.TButton"
                            )

    langley_button.grid(row=9, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    tyndall_button = Button(second_frame,
                            text='Mt. Tyndall',
                            command=lambda: add_and_print('Tyndall'),
                            style="peak.TButton"
                            )

    tyndall_button.grid(row=10, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    muir_button = Button(second_frame,
                         text='Mt. Muir',
                         command=lambda: add_and_print('Muir'),
                         style="peak.TButton"
                         )

    muir_button.grid(row=11, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    north_palisade_button = Button(second_frame,
                                   text='North Palisade',
                                   command=lambda: add_and_print('North_Palisade'),
                                   style="peak.TButton"
                                   )

    north_palisade_button.grid(row=12, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    sill_button = Button(second_frame,
                         text='Mt. Sill',
                         command=lambda: add_and_print('Sill'),
                         style="peak.TButton"
                         )

    sill_button.grid(row=13, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    middle_palisade_button = Button(second_frame,
                                    text='Middle Palisade',
                                    command=lambda: add_and_print('Palisade'),
                                    style="peak.TButton"
                                    )

    middle_palisade_button.grid(row=14, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    # Add Alaska/Washington Buttons ; Alaska/Washington column = 3
    denali_button = Button(second_frame,
                           text="Denali",
                           command=lambda: add_and_print('Denali'),
                           style="peak.TButton"
                           )

    denali_button.grid(row=4, column=3, padx=20, pady=5, ipadx=3, ipady=3)

    rainier_button = Button(second_frame,
                            text='Mt. Rainier',
                            command=lambda: add_and_print('Rainier'),
                            style="peak.TButton"
                            )

    rainier_button.grid(row=5, column=3, padx=20, pady=5, ipadx=3, ipady=3)

    # Add Colorado Buttons ; Colorado column = 4
    elbert_button = Button(second_frame,
                           text='Mt. Elbert',
                           command=lambda: add_and_print('Elbert'),
                           style="peak.TButton"
                           )

    elbert_button.grid(row=4, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    handies_button = Button(second_frame,
                            text='Handies Peak',
                            command=lambda: add_and_print('Handies'),
                            style="peak.TButton"
                            )

    handies_button.grid(row=5, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    grays_button = Button(second_frame,
                          text='Grays Peak',
                          command=lambda: add_and_print('Grays'),
                          style="peak.TButton"
                          )

    grays_button.grid(row=6, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    quandary_button = Button(second_frame,
                             text='Quandary Peak',
                             command=lambda: add_and_print('Quandary'),
                             style="peak.TButton"
                             )

    quandary_button.grid(row=7, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    san_luis_button = Button(second_frame,
                             text='San Luis Peak',
                             command=lambda: add_and_print('San_Luis'),
                             style="peak.TButton"
                             )

    san_luis_button.grid(row=8, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    pikes_button = Button(second_frame,
                          text='Pikes Peak',
                          command=lambda: add_and_print('Pikes'),
                          style="peak.TButton"
                          )

    pikes_button.grid(row=9, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    bierstadt_button = Button(second_frame,
                              text='Mt. Bierstadt',
                              command=lambda: add_and_print('Bierstadt'),
                              style="peak.TButton"
                              )

    bierstadt_button.grid(row=10, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    belford_button = Button(second_frame,
                            text='Mt. Belford',
                            command=lambda: add_and_print('Belford'),
                            style="peak.TButton"
                            )

    belford_button.grid(row=11, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    uncompahgre_button = Button(second_frame,
                                text='Uncompahgre Peak',
                                command=lambda: add_and_print('Uncompahgre'),
                                style="peak.TButton"
                                )

    uncompahgre_button.grid(row=12, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    shavano_button = Button(second_frame,
                            text='Mt. Shavano',
                            command=lambda: add_and_print('Shavano'),
                            style="peak.TButton"
                            )

    shavano_button.grid(row=13, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    humboldt_button = Button(second_frame,
                             text='Humboldt Peak',
                             command=lambda: add_and_print('Humboldt'),
                             style="peak.TButton"
                             )

    humboldt_button.grid(row=14, column=4, padx=20, pady=5, ipadx=3, ipady=3)

    # Add Colorado_2 Buttons ; Colorado_2 column = 5
    sherman_button = Button(second_frame,
                            text='Mt. Sherman',
                            command=lambda: add_and_print('Sherman'),
                            style="peak.TButton"
                            )

    sherman_button.grid(row=4, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    bross_button = Button(second_frame,
                          text='Mt. Bross',
                          command=lambda: add_and_print('Bross'),
                          style="peak.TButton"
                          )

    bross_button.grid(row=5, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    columbia_button = Button(second_frame,
                             text='Mt. Columbia',
                             command=lambda: add_and_print('Columbia'),
                             style="peak.TButton"
                             )

    columbia_button.grid(row=6, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    lincoln_button = Button(second_frame,
                            text='Mt. Lincoln',
                            command=lambda: add_and_print('Lincoln'),
                            style="peak.TButton"
                            )

    lincoln_button.grid(row=7, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    democrat_button = Button(second_frame,
                             text='Mt. Democrat',
                             command=lambda: add_and_print('Democrat'),
                             style="peak.TButton"
                             )

    democrat_button.grid(row=8, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    torreys_button = Button(second_frame,
                            text='Torreys Peak',
                            command=lambda: add_and_print('Torreys'),
                            style="peak.TButton"
                            )

    torreys_button.grid(row=9, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    huron_button = Button(second_frame,
                          text='Huron Peak',
                          command=lambda: add_and_print('Huron'),
                          style="peak.TButton"
                          )

    huron_button.grid(row=10, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    culebra_button = Button(second_frame,
                            text='Culebra Peak',
                            command=lambda: add_and_print('Culebra'),
                            style="peak.TButton"
                            )

    culebra_button.grid(row=11, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    princeton_button = Button(second_frame,
                              text='Mt. Princeton',
                              command=lambda: add_and_print('Princeton'),
                              style="peak.TButton"
                              )

    princeton_button.grid(row=12, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    red_cloud_button = Button(second_frame,
                              text='Red Cloud Peak',
                              command=lambda: add_and_print('Red_Cloud'),
                              style="peak.TButton"
                              )

    red_cloud_button.grid(row=13, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    evans_button = Button(second_frame,
                          text='Mt. Evans',
                          command=lambda: add_and_print('Evans'),
                          style="peak.TButton"
                          )

    evans_button.grid(row=14, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    sunshine_button = Button(second_frame,
                             text='Sunshine Peak',
                             command=lambda: add_and_print('Sunshine'),
                             style="peak.TButton"
                             )

    sunshine_button.grid(row=15, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    # Add to Colorado 3 ; Column 6
    yale_button = Button(second_frame,
                         text='Mt. Yale',
                         command=lambda: add_and_print('Yale'),
                         style="peak.TButton"
                         )

    yale_button.grid(row=4, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    massive_button = Button(second_frame,
                            text='Mt. Massive',
                            command=lambda: add_and_print('Massive'),
                            style="peak.TButton"
                            )

    massive_button.grid(row=5, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    oxford_button = Button(second_frame,
                           text='Mt. Oxford',
                           command=lambda: add_and_print('Oxford'),
                           style="peak.TButton"
                           )

    oxford_button.grid(row=6, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    antero_button = Button(second_frame,
                           text='Mt. Antero',
                           command=lambda: add_and_print('Antero'),
                           style="peak.TButton"
                           )

    antero_button.grid(row=7, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    harvard_button = Button(second_frame,
                            text='Mt. Harvard',
                            command=lambda: add_and_print('Harvard'),
                            style="peak.TButton"
                            )

    harvard_button.grid(row=8, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    capitol_button = Button(second_frame,
                            text='Capitol Peak',
                            command=lambda: add_and_print('Capitol'),
                            style="peak.TButton"
                            )

    capitol_button.grid(row=9, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    castle_button = Button(second_frame,
                           text='Castle Peak',
                           command=lambda: add_and_print('Castle'),
                           style="peak.TButton"
                           )

    castle_button.grid(row=10, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    windom_button = Button(second_frame,
                           text='Windom Peak',
                           command=lambda: add_and_print('Windom'),
                           style="peak.TButton"
                           )

    windom_button.grid(row=11, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    challenger_button = Button(second_frame,
                               text='Challenger Point',
                               command=lambda: add_and_print('Challenger'),
                               style="peak.TButton"
                               )

    challenger_button.grid(row=12, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    blanca_button = Button(second_frame,
                           text='Blanca Peak',
                           command=lambda: add_and_print('Blanca'),
                           style="peak.TButton"
                           )

    blanca_button.grid(row=13, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    sneffels_button = Button(second_frame,
                             text='Mt. Sneffels',
                             command=lambda: add_and_print('Sneffels'),
                             style="peak.TButton"
                             )

    sneffels_button.grid(row=14, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    lindsey_button = Button(second_frame,
                            text='Mt. Lindsey',
                            command=lambda: add_and_print('Lindsey'),
                            style="peak.TButton"
                            )

    lindsey_button.grid(row=15, column=6, padx=20, pady=5, ipadx=3, ipady=3)

    # Add Clear an Submit Buttons
    submit_button = Button(second_frame,
                           text='Submit',
                           command=lambda: load_selection(),
                           style='submit.TButton'
                           )

    submit_button.grid(row=20, column=5, padx=20, pady=5, ipadx=3, ipady=3)

    clear_button = Button(second_frame,
                          text='Clear Selection',
                          command=lambda: clear_selection(),
                          style='clear.TButton'
                          )

    clear_button.grid(row=20, column=2, padx=20, pady=5, ipadx=3, ipady=3)

    page_1_top.mainloop()
