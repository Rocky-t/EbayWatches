import sys
sys.path.insert(1,"../")
from listing_obj.listing import lo
from bs4 import BeautifulSoup
import requests
import re

#returns a webpage from a url
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

#returns overlap between keywords and words in listing name
def has_keyword(listing, keywords):
    return keywords.intersection(listing.lower().split(" "))

#will return a few ebay listing objects
class ebay_getter:
    def __init__(self, link:str,keywords:set):
        self._link = link
        self._keywords=keywords

    def get_listings(self):
        soup = BeautifulSoup(getHTMLdocument(self._link), 'html.parser')
        #get just the listings
        listings = soup.find("ul", {"class": "srp-results srp-grid clearfix"})\
                    .find_all("div", {"class": "s-item__wrapper clearfix"})
        
        #loop through all listings
        good_listings = []
        for item in listings:
            name = item.find("span", {"role": "heading"}).text
            if not name:
                continue
            trigger = has_keyword(name, self._keywords)
            if len(trigger) == 0:
                continue
            image = item.find("img")['src']
            link = item.find("a")['href']
            price = item.find("span",{"class": "s-item__price"}).text 
            list_obj = lo(name,price,link,image,trigger)
            good_listings.append(list_obj)

        return good_listings

