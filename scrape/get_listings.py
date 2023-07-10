import sys
sys.path.insert(1,"../")
from listing_obj.listing import lo
from bs4 import BeautifulSoup
import time
import requests

#returns a webpage from a url
def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

#returns overlap between keywords and words in listing name
def has_keyword(listing, keywords):
    return keywords.intersection(listing.lower().split(" "))

def get_float_price(price):
    """Special way to get ebay listings because sometimes they are <$16.99 to 24.99> format
       probably should have used re but this works fine and was quick
    """
    prices = price.split(" ")
    price = prices[0]
    nums = {'1','2','3','4','5','6','7','8','9','.','0'}
    p = ""
    for char in price:
        p += char if char in nums else ""
    return float(p)

class ebay_getter:
    def __init__(self, link:str,keywords:dict,negative_keywords:dict={}):
        self._link = link
        self._keywords=keywords
        self._negative_keywords = negative_keywords
        self._cur_top = None
        self._old_top = None
        self._links = set()

    def get_listings(self):
        """
        Returns a list of listing objects that meet the given criteria
        """
        if (time.time() % 86400) < 30 and len(self._links) != 0:
            self._links = set()
        try:
            #we do this every time so we can flip throguh pages
            soup = BeautifulSoup(getHTMLdocument(self._link), 'html.parser')
            #get just the listings
            listings = soup.find("ul", {"class": "srp-results srp-grid clearfix"})\
                        .find_all("div", {"class": "s-item__wrapper clearfix"})
        except:
            return []
        #loop through all listings
        good_listings = []
        for i in range(len(listings)):
            try:
                item = listings[i]
                name = item.find("span", {"role": "heading"}).text
                print(name)
                keys = {key for key in self._keywords}
                trigger = has_keyword(name, keys)
                #no triggers found or womens watch, move on
                if len(trigger) == 0 or len(has_keyword(name,self._negative_keywords))>0:
                    continue
                price = get_float_price(item.find("span",{"class": "s-item__price"}).text)
                if len(trigger) == 1 and self._keywords[list(trigger)[0]] < price:
                    continue
                link = item.find("a")['href']
                image = item.find("img")['src']
                list_obj = lo(name,price,link,image,trigger)

                if name not in self._links:
                    good_listings.append(list_obj)
                    self._links.add(name)
                else:
                    continue
            except:
                continue
        return good_listings

