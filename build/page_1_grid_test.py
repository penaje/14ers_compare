from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk
from tkinter.ttk import *

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


# Add Peaks function
def print_peaks(peak_name):
    string_1 = ' & '.join([str(elem) for elem in info.selected_peaks])
    selected_peaks_label_input.configure(text=string_1)
    print('this is my string:' + string_1)


# Call two functions for the buttons
def add_and_print(peak_name):
    add_button_name_to_selection(peak_name)
    print_peaks(peak_name)


def clear_selection():
    """Clears the user selection"""
    info.selected_peaks.clear()
    selected_peaks_label_input.configure(text='')


root = Tk()
root.title('Please Select Your Peaks!')
root.geometry("600x500")
root.configure(bg="#FFFFFF")

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

# Add Styles
style = ttk.Style(root)
style.theme_use('clam')
style.configure('peak.TButton', font=('calibri', 10, 'bold'), foreground='black', background="#BF40BF")
style.configure('clear.TButton', font=('calibri', 10, 'bold'), foreground='black', background='red')
style.configure('submit.TButton', font=('calibri', 10, 'bold'), foreground='black', background="#00FFFF")

style.map('peak.TButton', background=[('pressed', 'blue'),
                                      ('active', 'green')])
# Add Labels
title_label = Label(second_frame, text='14er Comparison Tool!', font=('roboto', 20, 'bold'))

title_label.grid(row=0, column=0, columnspan=6, padx=5, pady=2, ipadx=3, ipady=3)

selection_label = Label(second_frame, text='Please select two to three peaks to compare!',
                        font=('calibri', 14, 'bold')
                        )

selection_label.grid(row=1, column=1, columnspan=5, padx=5, pady=2, ipadx=3, ipady=3)

selected_peaks_label_title = Label(second_frame, text='Here are your selected peaks:', font=('arial', 12, 'italic'))
selected_peaks_label_title.grid(row=2, column=1, columnspan=3)

selected_peaks_label_input = Label(second_frame, font=('arial', 12, 'bold'))
selected_peaks_label_input.grid(row=2, column=4, columnspan=2)

california_label = Label(second_frame, text='California',
                         font=('calibri', 14, 'bold'))

california_label.grid(row=3, column=2, padx=10, pady=2, ipadx=3, ipady=3)

alaska_label = Label(second_frame, text='Alaska',
                     font=('calibri', 14, 'bold'))

alaska_label.grid(row=3, column=3, padx=10, pady=2, ipadx=3, ipady=3)

colorado_label = Label(second_frame, text='Colorado',
                       font=('calibri', 14, 'bold'))

colorado_label.grid(row=3, column=4, padx=10, pady=2, ipadx=3, ipady=3)

washington_label = Label(second_frame, text='Washington',
                         font=('calibri', 14, 'bold'))

washington_label.grid(row=3, column=5, padx=10, pady=2, ipadx=3, ipady=3)

# Add  California buttons
whitney_button = Button(second_frame,
                        text="Mt. Whitney",
                        command=lambda: add_and_print('Whitney'),
                        style="peak.TButton"
                        )

whitney_button.grid(row=4, column=2, padx=20, pady=5, ipadx=3, ipady=3)

shasta_button = Button(second_frame,
                       text='Mt.Shasta',
                       command=lambda: add_and_print('Shasta'),
                       style="peak.TButton"
                       )

shasta_button.grid(row=5, column=2, padx=20, pady=5, ipadx=3, ipady=3)  # California column = 2

# Add Alaska Buttons
denali_button = Button(second_frame,
                       text="Denali",
                       command=lambda: add_and_print('Denali'),
                       style="peak.TButton"
                       )

denali_button.grid(row=4, column=3, padx=20, pady=5, ipadx=3, ipady=3)  # Alaska column = 3

# Add Colorado Buttons
elbert_button = Button(second_frame,
                       text='Mt. Elbert',
                       command=lambda: add_and_print('Elbert'),
                       style="peak.TButton"
                       )

elbert_button.grid(row=4, column=4, padx=20, pady=5, ipadx=3, ipady=3)  # Colorado column = 4

# Add Washington Buttons
rainier_button = Button(second_frame,
                        text='Mt. Rainier',
                        command=lambda: add_and_print('Rainier'),
                        style="peak.TButton"
                        )

rainier_button.grid(row=4, column=5, padx=20, pady=5, ipadx=3, ipady=3)

# Add Clear an Submit Buttons
submit_button = Button(second_frame,
                       text='Submit',
                       command=lambda: load_page_2(),
                       style='submit.TButton'
                       )

submit_button.grid(row=6, column=5, padx=20, pady=5, ipadx=3, ipady=3)

clear_button = Button(second_frame,
                      text='Clear Selection',
                      command=lambda: clear_selection(),
                      style='clear.TButton'
                      )

clear_button.grid(row=6, column=2, padx=20, pady=5, ipadx=3, ipady=3)

root.mainloop()