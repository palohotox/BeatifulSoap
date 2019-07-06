
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv


# Define Url to get the data from
myurl= "https://www.allyoucanread.com/uk-car/"
#Country, type, URL and Service name


# Opening connection grabbing the page
uClient= uReq(myurl)
pageHtml= uClient.read()
page_soup=soup(pageHtml,"html.parser")


#grab each products
container = page_soup.findAll("div",{"class":"wrapper clearfix"})

item = container[0]

print(item)
#container = page_soup.div.div.div
"""
for item in container:
    # brandName include error handling
    # brand = item.find("a", {"class": "item-brand"}).img["title"]
    # print(brand)
    url = item.find("a", {"class": "sublink"}).text
    # Getting text out of anchor
    #itemName = item.find("a", {"class": "item-title"}).text
    # Get a Price

    #price = item.find("div", {"class": "item-action"}).find("li", {"class": "price-current"}).text

    print(url)
"""

