import pandas as pd
import requests
import unicodedata
from bs4 import BeautifulSoup
import json
import sys

# This is my aircraft scraper service for my teammate

with open('input.json') as file:
    data = json.load(file)


# This code snippet from:
# https://stackoverflow.com/questions/14596884/remove-text-between-and

def remove_text_inside_brackets(text, brackets="[]"):
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


statistics = ['crew', 'length', 'wingspan', 'swept wingspan', 'wing area', 'aspect ratio', 'max takeoff weight',
              'powerplant', 'maximum speed', 'ferry range', 'range', 'combat range', 'wing loading',
              'thrust/weight']

plane = data.get('TARGET')

url = "https://en.wikipedia.org/wiki/" + plane

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

try:  # Error Handling
    dfs = pd.read_html(page.text)
except ValueError:
    output_JSON = {'COMMAND': "SCRAPE_FAIL", 'TARGET': 'NULL'}
    with open('output.json', 'w') as outfile:
        json.dump(output_JSON, outfile)
    sys.exit("SCRAPE FAIL")

first_tag = soup.find('b', string='General characteristics')

if first_tag is None:  # Error Handling
    output_JSON = {'COMMAND': "SCRAPE_FAIL", 'TARGET': 'NULL'}
    with open('output.json', 'w') as outfile:
        json.dump(output_JSON, outfile)
    sys.exit("SCRAPE FAIL")
else:
    general_stats_tag = first_tag.parent.parent

general_stats = general_stats_tag.next_sibling

performance_tag = general_stats.next_sibling.next_sibling

performance_stats = performance_tag.next_sibling.next_sibling

armament_tag = performance_stats.next_sibling.next_sibling

armament_stats = armament_tag.next_sibling.next_sibling

general_stats_dict = {}
performance_stats_dict = {}
armament_stats_dict = {}


def merge_2(dict1, dict2):
    res = {**dict1, **dict2}
    return res


stats_list = [general_stats, performance_stats, armament_stats]

for stats in stats_list:

    for element in stats.find_all('li'):
        key = element.find('b')
        if key is not None:
            proper_key = key.text
            temp_value = []
            count = 0
            for child in element.stripped_strings:
                if count == 0:
                    count += 1
                    next(element.stripped_strings)
                else:
                    temp_value.append(child)
                    count += 1
            formatted_key = proper_key[:-1].upper()
            clean_text = unicodedata.normalize("NFKD", ' '.join(temp_value))
            new_clean_text = remove_text_inside_brackets(clean_text)
            if stats == general_stats:
                general_stats_dict[formatted_key] = new_clean_text.replace('×', '')
            if stats == performance_stats:
                performance_stats_dict[formatted_key] = new_clean_text.replace('×', '')
            if stats == armament_stats:
                armament_stats_dict[formatted_key] = new_clean_text.replace('×', '')
    if stats == performance_stats:
        thrust_weight_string = performance_stats_dict.get(
            'THRUST/WEIGHT')  # remove ':' at the beginning of THRUST/WEIGHT
        performance_stats_dict['THRUST/WEIGHT'] = thrust_weight_string[2:]


first_merged_dict = merge_2(general_stats_dict, performance_stats_dict)

temp_dict = {}

for stat in statistics:  # Removes unnecessary stats from the dictionary
    if stat.upper() in first_merged_dict.keys():
        temp_dict[stat.upper()] = first_merged_dict.get(stat.upper())
    else:
        temp_dict[stat.upper()] = 'NULL'

final_dict = merge_2(temp_dict, armament_stats_dict)

json_object = json.dumps(final_dict, indent=2)

output_JSON = {'COMMAND': "SCRAPE_SUCCESS", 'TARGET': final_dict}

with open('output.json', 'w') as outfile:
    json.dump(output_JSON, outfile)

print("File Successfully Generated")
