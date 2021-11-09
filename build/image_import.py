from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from urllib.request import urlopen
import urllib
import io
import info
import json
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context


def check_image_size(url):
    """Returns True if the image is large enough"""

    def img_from_url(url):
        with urllib.request.urlopen(url) as connection:
            raw_data = connection.read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        return image

    window = Tk()

    image_one = img_from_url(url)
    width = image_one.width()
    height = image_one.height()

    if (width or height) < 150:
        return False
    else:
        return True


def import_images(selected_peaks):  # Pass it the selected_peaks list
    base_url = 'https://en.wikipedia.org/wiki/'

    image_list = []

    for peak in selected_peaks:
        input_json = {'COMMAND': 'SCRAPE', 'TARGET': base_url + info.peaks_url.get(peak)}

        with open('input.json', 'w') as outfile:  # Create the input.json
            json.dump(input_json, outfile)

        exec(open("./image_scraper/image_scraper.py").read())

        with open('output.json') as file:  # Output the json file with URL's 1st time
            data = json.load(file)

        count = 0

        while check_image_size('https:' + data.get('URLS')[count]) is not True:
            # This verifies that the image is large enough to be correct
            count += 1

        updated_url = 'https:' + data.get('URLS')[count]

        image_list.append(updated_url)

    return image_list



