import requests
from bs4 import BeautifulSoup
import json


f = open('input.json',)

data = json.load(f)

# print(data['TARGET'])


def getdata(url):
    r = requests.get(url)
    return r.text


htmldata = getdata(data['TARGET'])
soup = BeautifulSoup(htmldata, 'html.parser')

url_list = []
for item in soup.find_all('img'):
    url_list.append(item['src'])
    # print(item['src'])

return_dict = {
    "COMMAND": "SCRAPE_SUCCESS",
    "URLS": url_list
}


with open("output.json", "w") as outfile:
    json.dump(return_dict, outfile)