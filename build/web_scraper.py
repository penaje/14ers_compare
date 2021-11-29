import requests
from bs4 import BeautifulSoup

URL = "https://www.peakbagger.com/peak.aspx?pid=2477"

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
info_dict['State'] = info

# Get Coordinates

coord = soup.find('td', string="Latitude/Longitude (WGS84)")
temp_list = []
info = coord.next_sibling.stripped_strings
for num in info:
    temp_list.append(num)
info_dict['Coordinates'] = temp_list[1][:-10]

print(info_dict)









