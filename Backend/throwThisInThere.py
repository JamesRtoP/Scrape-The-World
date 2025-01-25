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

#allBreakFast = soup.select('#Breakfast h4, #Breakfast h3')
#if False:
#    tre = soup.find("h3", "diningVenueName")
#    station1 = tre.text
#    tre = tre.find_next("h3", "diningVenueName")
#    tre = tre.find_previous('h4')
#    tre = tre.find_next("h3", "diningVenueName")

Breakfast = {}
Lunch = {}
Dinner = {}

Brunch = {}

tre = soup.find("div", id = "Breakfast")
stationNum = tre.find("h3", "diningVenueName")
    #station1 = station1.find_next("h3", "diningVenueName")
    #pizza = tre.findAll("h3", "diningVenueName")

#allh3 = tre.find_all("h3")
#for i in tre:
#    print(i)

line = tre.find()
if "diningMenuItem" in line:

print (line)
#station = tre.find("h3", "diningVenueName")

#foodItem = station.find_next_sibling()

#nextS = nextS.find_previous_sibling()
#allergen = foodItem.find_next_sibling()
#unicode = str(foodItem)
#print( unicode)
#word = "class"
#if word in unicode:
#    print("yes")
#else:
#    print("no")
#nextS = nextS.find_next_sibling()

#.get
#print (len(allh3))

#child of h3
#child of h4

#breakFastItems =  soup.select_one('#Breakfast h3')


#breakFastItems =  soup.find_all("h3", class_ = 'diningVenueName')#, id = 'Breakfast')

#print (breakFastItems)
#print (station)
#print (foodItem)
#print (allergen)


#items = []
#Fast = {}
#for i in tre:
#    print(i)
#    #print (i.find)
#    print("\n")
    
    

#print(r.content[:100])
#print("Yeah")