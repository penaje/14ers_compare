import requests
from bs4 import BeautifulSoup


def info_box_scrape(URL):
    """Scrapes peakbaggers.com for info for info boxes"""

    # This code snippet from:
    # https://stackoverflow.com/questions/14596884/remove-text-between-and

    def remove_text_inside_brackets(text, brackets="()"):
        count = [0] * (len(brackets) // 2)  # count open/close brackets
        saved_chars = []
        for character in text:
            for i, b in enumerate(brackets):
                if character == b:
                    kind, is_close = divmod(i, 2)
                    count[kind] += (-1) ** is_close
                    if count[kind] < 0:
                        count[kind] = 0
                    else:
                        break
            else:
                if not any(count):
                    saved_chars.append(character)
        return ''.join(saved_chars)

    # Denali edge case handler
    if URL == "https://www.peakbagger.com/peak.aspx?pid=271":
        info_dict = {'Elevation': '20,310 ft (6190 m)', 'Prominence': '20,194 ft (6,155 m)', 'State': 'Alaska',
                     'Isolation': '4,621.1 mi (7,436.9 km)', 'Coordinates': '63.069042, -151.006347'}
        return info_dict

    r = requests.get(URL)

    soup = BeautifulSoup(r.content, 'html.parser')

    info_dict = {}

    # Get Elevation info
    elevation = soup.find('td', string='Elevation Info:')
    info = elevation.next_sibling

    temp_list = []
    for strings in info.stripped_strings:
        temp_list.append(strings)

    info_dict['Elevation'] = temp_list[1][2:]

    # Get Prominence info
    prominence = soup.find('a', string='Clean Prominence')
    info = prominence.next_sibling
    info_dict['Prominence'] = info[2:]

    # Get Isolation

    isolation = soup.find('a', string='Isolation')
    info = isolation.parent.next_sibling
    temp_list = []
    count = 0
    for string in info.stripped_strings:
        temp_list.append(string)
    info_dict['Isolation'] = temp_list[2][10:]

    # Get State

    state = soup.find('td', string="State/Province")
    info = state.next_sibling.string
    info_dict['State'] = remove_text_inside_brackets(info)

    # Get Coordinates

    coord = soup.find('td', string="Latitude/Longitude (WGS84)")
    temp_list = []
    info = coord.next_sibling.stripped_strings
    for num in info:
        temp_list.append(num)
    info_dict['Coordinates'] = temp_list[1][:-10]

    return info_dict
