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

def fillMealTime(soup, mealTimeName):
    mealTime = []#What will be returned, i.e. for lunch will list everything avialabe

    tre = soup.find("div", id = mealTimeName)#gets the mealTime html by itself
    Station = { #each station will have a name and a list of items at it
    "station":"",
    "menuItems": [] 
    }

    menuItem = None #menu food item
    line = tre.find_next()#get first line of the meal time
    while(line != None):

        lineStr = str(line)#make line a string to find which type it is
        if "diningMenuItem" in lineStr:#is menuItem
            menuItem = line.text
        elif "allergens-and-diets" in lineStr:#is allergen
            foodPair = (menuItem,handleAllergens(line))
            Station["menuItems"].append(foodPair)
        elif "diningVenueName" in lineStr:#is a station
            if Station["station"] != "": #if station name is not undefined, place it into meal (i.e breakfast lunch or dinner)
                mealTime.append(Station.copy())#add full station to mealTime
                Station["menuItems"] = []#clear Station
            Station["station"] = line.text#set station name
        line = line.find_next_sibling()#move onto next line

    mealTime.append(Station)#add the last station after the loop
    return mealTime


url = 'https://dining.wsu.edu/southside-cafe'

#r = requests.get(url)
#save_html(r.content, 'figherP')
cont = open_html('figherP')
#save_html(cont, 'friday')

soup = BeautifulSoup(cont, 'html.parser')


#getting just the day from soup
day = soup.select_one(".secondary.disabled.menuButton").text.split()[0]
if day == "Saturday" or day == "Sunday":
    Brunch = fillMealTime(soup, "Brunch")
    printL (Brunch)

else:
    Breakfast = fillMealTime(soup, "Breakfast")
    printL (Breakfast)




#stationNum = tre.find_all("h3", "diningVenueName")















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