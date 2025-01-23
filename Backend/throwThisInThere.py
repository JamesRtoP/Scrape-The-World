import requests
from bs4 import BeautifulSoup

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


    
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

url = 'https://bellator.com/regular-fighter/magomed-magomedkerimov'

#r = requests.get(url)
cont = open_html('fighterP')
save_html(r.content, 'figherP')

soup = BeautifulSoup(r.content, 'html.parser')

#fighterPortrait = soup.select_one('.hero-profile__image')
fighterStats = soup.select('img[src *= "bodyShots"]')

#)

print (fighterStats)

#print(r.content[:100])
#print("Yeah")