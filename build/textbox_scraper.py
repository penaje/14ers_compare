import requests
from bs4 import BeautifulSoup


def get_textbox_info(peak_name):
    """Returns either the climbing info or the basic mountain information if no climbing info"""
    import info

    url_start = "https://en.wikipedia.org/wiki/"

    print(peak_name)

    r = requests.get(url_start + info.peaks_url.get(peak_name))

    soup = BeautifulSoup(r.content, 'html.parser')

    # Looks to see if climbing info exists
    climbing_info = soup.find(id="Climbing")

    if climbing_info is not None:
        parent = climbing_info.parent

        list_to_join = []

        paragraphs = parent.find_next_siblings('p')
        for item in paragraphs:
            for string in item.stripped_strings:
                list_to_join.append(string)

        climbing_info = ' '.join(list_to_join)

        return climbing_info

    else:

        string_to_find = info.peaks_title.get(peak_name)

        # Finds the start of the description with the given peaks name
        info = soup.find("b", string=string_to_find)

        list_to_join = []

        for item in info.parent.stripped_strings:
            list_to_join.append(item)

        # This is the basic info for the peak from wikipeadia page
        paragraph = ' '.join(list_to_join)

        return paragraph

