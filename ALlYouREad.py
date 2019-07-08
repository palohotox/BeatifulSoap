
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import csv

def get_imd_item_info(item):
    #movie_title = movie.a.contents[0]
    #movie_year = movie.span.contents[0]
    url = item.find('a',{"class": "sublink"}).attrs['href']

    return url

def get_category(countryurl,country):

    cat = ['classifieds', 'car', 'job', 'realEstate']

    for categ in cat:

        # replace newspapers with categories 'https: // www.allyoucanread.com / afghanistan - newspapers /'
        caturl= countryurl.rsplit('-', 1)[0] +'-'+ categ

        #print(caturl)
        get_info(caturl,country,categ)

        break

        #myurl1 = countryurl

        #uClient = uReq(myurl1)
        #pageHtml = uClient.read()
        #page_soup = soup(pageHtml, "html.parser")


    return caturl

def get_info(infourl,country,categ):


    myurl1 = infourl

    uClient = uReq(myurl1)
    pageHtml = uClient.read()
    page_soup = soup(pageHtml, "html.parser")

    # grab each products
    container = page_soup.findAll("div", {"class": "wrapper clearfix"})

    # show the attribute
    # print(item.find('a',{"class": "sublink"} ).attrs['href'])

    # print(len(container))
    for item in container:
        myurl = item.findAll('a', {"class": "sublink"})  # ,limit=5

        # loop through the result list and return the component
        for url in myurl:
            print(country,categ,url['href'])




#Loop through Country
myurl1= 'https://www.allyoucanread.com/'

uClient= uReq(myurl1)
pageHtml= uClient.read()
page_soup=soup(pageHtml,"html.parser")

conturlmain = page_soup.findAll('select',{"name":"az"})

#conturlmain = conturlmain[0]
#print(conturlmain[0])

for conturlm in conturlmain:
    conturlopt =  conturlm.findAll('option')

    count = 0

    for contopt in conturlopt:

       if count > 5 :
        #print(contopt['value'])
        #print(contopt)
        countryurl=contopt['value']

        #Call function for get_category
        get_category(countryurl,contopt.text)


       count=count+1

#SAMPLE FOR AFGHANISTAN
#"https://www.allyoucanread.com/afghanistan-newspapers/"



"""
# Define Url to get the data from
myurl= "https://www.allyoucanread.com/uk-car/"
#Country, type, URL and Service name

# Opening connection grabbing the page
uClient= uReq(myurl)
pageHtml= uClient.read()
page_soup=soup(pageHtml,"html.parser")



"""
