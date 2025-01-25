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

def handleAllergens(allergenLine):
    dietary = []
    allergen = []
    for i in allergenLine.select(".mealTypes .requirement"):
        dietary.append(i.text)
    for i in allergenLine.select(".allergens .allergen"):
        allergen.append(i.text)
    return (dietary, allergen)

url = 'https://dining.wsu.edu/southside-cafe'

#r = requests.get(url)
#save_html(r.content, 'figherP')
cont = open_html('figherP')
save_html(cont, 'friday')

soup = BeautifulSoup(cont, 'html.parser')

#getting just the day from soup
weekday = True
day = soup.select_one(".secondary.disabled.menuButton").text.split()[0]
if day == "Saturday" or day == "Sunday":
    weekday = False

mealTime = []

tre = soup.find("div", id = "Lunch")
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
    if "diningMenuItem" in lineStr:#is menuItem
        menuItem = line.text
    elif "allergens-and-diets" in lineStr:#is allergen
        allergens = lineStr
        foodPair = (menuItem,handleAllergens(line))
        Station["menuItems"].append(foodPair)
    elif "diningVenueName" in lineStr:#is a station
        if Station["station"] != "": #if station name is not undefined, place it into meal (i.e breakfast lunch or dinner)
            mealTime.append(Station.copy())
            Station["menuItems"] = []
        Station["station"] = line.text

    line = line.find_next_sibling()#move onto next line

mealTime.append(Station)
printL (mealTime)










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