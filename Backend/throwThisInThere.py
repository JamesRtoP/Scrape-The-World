import requests
from bs4 import BeautifulSoup
#from tqdm import tdqm_notebook

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


    
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()

url = 'https://dining.wsu.edu/southside-cafe'

#r = requests.get(url)
#save_html(r.content, 'figherP')
cont = open_html('figherP')

soup = BeautifulSoup(cont, 'html.parser')

#breakfast = soup.select('.accordion-item h3')
breakfast = soup.select('#Breakfast h4, #Breakfast h3')
#breakfast = soup.select('.accordion-item h3')

#fighterPortrait = soup.select_one('.hero-profile__image')
#fighterPortrait = soup.select_one('img[src *= "bodyshots"]')['src']
#eventually I will remove 
#fighterName = soup.select_one('.container.text-shadow h1').text.strip()
#)


#breakFastItems =  soup.select_one('#Breakfast h3')
breakFastItems =  soup.find(id = 'Breakfast', )

print (breakFastItems)
#print (breakfast)
#for i in breakFastItems:
#    print(i)
#    print("\n")

#print(r.content[:100])
#print("Yeah")