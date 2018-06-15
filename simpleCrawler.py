import requests
import webbrowser
import time
from bs4 import BeautifulSoup
import json

results = []
ROOT_URL = "http://mp3teca.com/bad-bunny/"
for current_page in range(1):
    content = requests.get(ROOT_URL)
    soup = BeautifulSoup(content.text, "html.parser")
    items_container = soup.find(id='mp3s')

for ultag in soup.find_all(id='mp3s'):
    for link in ultag.find_all('a'):
        results.append(link.get('href'))

newResults = []
for url in results[0:len(results)]:
    content = requests.get(url)
    soup = BeautifulSoup(content.text, "html.parser")
    for link in soup.find_all('a', {'class': 'btn-d-album'}):
        newResults.append(link.get('href'))

finalResults = []
for url in newResults[0:len(newResults)]:
    if url == '#':
        print("Esta URL no me sirve, voy a por ti Bad Bunny")
    else:
        content = requests.get(url)
        soup = BeautifulSoup(content.text, "html.parser")
        for link in soup.find_all(id='nwo'):
            for link2 in link.find_all('a'):
                finalResults.append(link2.get('href'))
                webbrowser.get('chrome %s').open(link2.get('href'), new=2, autoraise=True)
                time.sleep(10)


print(finalResults)

print("OK YA TE TENGO BAD BUNNY")

print("Done")

with open("results.json", "w") as results_file:
    json.dump(finalResults, results_file, indent=4, sort_keys=True)
