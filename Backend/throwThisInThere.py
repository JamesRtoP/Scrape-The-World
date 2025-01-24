import requests
from bs4 import BeautifulSoup
from tqdm import tdqm_notebook

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


    
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

url = 'https://bellator.com/regular-fighter/magomed-magomedkerimov'

#r = requests.get(url)
cont = open_html('figherP')
#save_html(r.content, 'figherP')

soup = BeautifulSoup(cont, 'html.parser')

#fighterPortrait = soup.select_one('.hero-profile__image')
fighterPortrait = soup.select_one('img[src *= "bodyshots"]')['src']
#eventually I will remove 
fighterName = soup.select_one('.container.text-shadow h1').text.strip()
#)

print (fighterPortrait)

#print(r.content[:100])
#print("Yeah")