from tkinter import *
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
    """Returns True if the image is the correct size"""

    def img_from_url(url):
        """Returns an Image object from a url string"""
        with urllib.request.urlopen(url) as connection:
            raw_data = connection.read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        return image

    image = img_from_url(url)
    width = image.width()
    height = image.height()

    if (width or height) < 150:
        return False
    else:
        return True


def import_images(selected_peaks):
    """Creates a list of image urls to be rendered into page 2 from the user selected peaks"""

    base_url = 'https://en.wikipedia.org/wiki/'

    image_list = []

    for peak in selected_peaks:
        # This will run each of the peaks that the user selected through
        # teammates service to grab image urls from the peaks wikipedia page.

        input_json = {'COMMAND': 'SCRAPE', 'TARGET': base_url + info.peaks_url.get(peak)}  # Request format

        with open('input.json', 'w') as outfile:  # Creates the input.json for teammates service to read
            json.dump(input_json, outfile)

        exec(open("./image_scraper/image_scraper.py").read())  # Run teammates service in separate process

        with open('output.json') as file:  # Reads the output file generated by teammates service
            data = json.load(file)

        count = 0

        while check_image_size('https:' + data.get('URLS')[count]) is not True:
            # This verifies that the image is large enough to be correct
            # if not we check the next image.
            # TODO need to add more/better logic, but it works for now
            count += 1
        updated_url = 'https:' + data.get('URLS')[count]
        image_list.append(updated_url)

    return image_list

