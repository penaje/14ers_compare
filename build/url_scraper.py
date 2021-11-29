import requests
from bs4 import BeautifulSoup
import json

# This was only run once to assist with populating my url's dictionary for peakbaggers.com instead of manually doing it.

ca_url = 'https://www.peakbagger.com/list.aspx?lid=-301603'

co_url = "https://www.peakbagger.com/list.aspx?lid=50080"

r = requests.get(co_url)

soup = BeautifulSoup(r.content, 'html.parser')

url_dict = {}

# Run for colorado Peaks

temp_list = []

info = soup.find_all('a')
count = 1
for item in info:
    if count >= 21:
        if item.string != 'Sierra Nevada':
            url_dict[item.string] = "https://www.peakbagger.com/" + str(item.get('href'))
        count += 1
    else:
        count += 1

r = requests.get(ca_url)

# Run for California peaks

r_2 = requests.get(ca_url)

soup = BeautifulSoup(r_2.content, 'html.parser')

temp_list = []

info = soup.find_all('a')
count = 1
for item in info:
    if count >= 21:
        if item.string != 'Sierra Nevada':
            url_dict[item.string] = "https://www.peakbagger.com/" + str(item.get('href'))
        count += 1
    else:
        count += 1

with open("peak_bagger_links.json", "w") as outfile:
    json.dump(url_dict, outfile)