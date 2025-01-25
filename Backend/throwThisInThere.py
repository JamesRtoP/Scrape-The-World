import requests
from bs4 import BeautifulSoup
#from tqdm import tdqm_notebook

#saving html that has been gotten
def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)


#open saved html
def open_html(path):
    with open(path, 'rb') as f:
        return f.read()
    
def printL(L):
    for i in L:
        print (i)

def handleAllergen(allergenLine):
    return allergenLine.text

url = 'https://dining.wsu.edu/southside-cafe'

#r = requests.get(url)
#save_html(r.content, 'figherP')
cont = open_html('figherP')

soup = BeautifulSoup(cont, 'html.parser')

#getting just the day from soup
weekday = True
day = soup.select_one(".secondary.disabled.menuButton").text.split()[0]
if day == "Saturday" or day == "Sunday":
    weekday = False


Breakfast = []
Lunch = []
Dinner = []

Brunch = []

tre = soup.find("div", id = "Breakfast")
stationNum = tre.find_all("h3", "diningVenueName")

Station = {
    "station":"",
    "menuItems": [] 
    }

menuItem = None
allergens = None

line = tre.find_next()
while(line != None):

    lineStr = str(line)#make line a string to find which type it is
    if "diningMenuItem" in lineStr:
        #Station["menuItems"].append(line.text)
        menuItem = line.text
    elif "allergens-and-diets" in lineStr:
        allergens = lineStr
        foodPair = (menuItem,allergens)
        Station["menuItems"].append(foodPair)
        #print ()
    elif "diningVenueName" in lineStr:
        #print(line.text)
        if Station["station"] != "": #if station name is not undefined, place it into breakfast
            Breakfast.append(Station.copy())
            Station["menuItems"] = []
            #Station["menuItems"].append("Yeah")
            #printL (Breakfast)
            #print ()


        Station["station"] = line.text
    

    line = line.find_next_sibling()

Breakfast.append(Station)
printL (Breakfast)










#station1 = station1.find_next("h3", "diningVenueName")
#pizza = tre.findAll("h3", "diningVenueName")

#allh3 = tre.find_all("h3")
#for i in tre:
#    print(i)



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