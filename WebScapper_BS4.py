
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# Define Url to get the data from
myurl= "https://www.newegg.com/global/my-en/?nm_mc=KNC-GoogleMYAdwords&cm_mmc=KNC-GoogleMYAdwords-_-BrandingExact-_-Newegg-_-Global&gclid=Cj0KCQjwgezoBRDNARIsAGzEfe7ohVHw2hpebnNRL8lHxxQLmxR47ujZGkZ8tbtisNoDZa2PkSELWUsaAhChEALw_wcB"

# Opening connection grabbing the page
uClient= uReq(myurl)
pageHtml= uClient.read()

page_soup=soup(pageHtml,"html.parser")
#uClient.close

#grab each products
itemDtl = page_soup.findAll("div",{"class":"item-container"})
#check len of container itemDtl
#len(itemDtl)

#get first item
#itemDtl[0]  - This we show the postscript of HTML
# Study that HTML and grab the information out of it

#item = itemDtl[0]
#grab item inside div
#item.div.a


#Loop through container

for item in itemDtl:
    print(item.div.a["href"])




