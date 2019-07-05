
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

#def strip_chars(str, chars):
#    return "".join(c for c in str if c not in chars)

# Define Url to get the data from
myurl= "https://www.newegg.com/global/my-en/p/pl?N=101591470&srchInDesc=GRAPHIC&Order=BESTSELLING"

# Opening connection grabbing the page
uClient= uReq(myurl)
pageHtml= uClient.read()
page_soup=soup(pageHtml,"html.parser")
#uClient.close

#grab each products
itemDtl = page_soup.findAll("div",{"class":"item-container"})
#check len of container itemDtl
#len(itemDtl)
#print(len(itemDtl))

#get first item
#itemDtl[0]  - This we show the postscript of HTML
# Study that HTML and grab the information out of it

#item = itemDtl[0]
#grab item inside div
#item.div.a

#price = item.find("div",{"class":"item-action"}).find("li",{"class":"price-current"}).text
#print(price.find("li",{"class":"price-current"}).text)

#Call a function to strip certain character in as string
#pricefinal = strip_chars(price,"-")

#rstrip() - function to strip new line "/n"
#print(pricefinal.rstrip())

#print(itemName)

#Initialize CSV
with open('graphic.csv', mode='w' , newline='') as myfile:
    my_write = csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #Loop through container
    for item in itemDtl:
        # brandName include error handling
        #brand = item.find("a", {"class": "item-brand"}).img["title"]
        #print(brand)
        brand="sample"
        # Getting text out of anchor
        itemName = item.find("a", {"class": "item-title"}).text
        # Get a Price

        price = item.find("div",{"class":"item-action"}).find("li",{"class":"price-current"}).text

        my_write.writerow([brand, itemName, price])
        """
        if brand:
            print(brand)
        else:
            print("N/A")
       """

        #print(itemName)
        #print (price)






