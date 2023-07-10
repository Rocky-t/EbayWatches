import sys
from bs4 import BeautifulSoup
import time
import csv
sys.path.insert(1,"../")
from scrape.get_listings import getHTMLdocument
"""
This file will collect image data on various types of watches for training a NN
There is no existing dataset, so we will have to scrape it
"""

class get_link_csv:
    def __init__(self, keywords:list, filename:str="watches.csv"):
        self._keywords = keywords
        self._filename = filename

    def get_search(self, watchbrand, pagenum:int=0):
        link_head = "https://www.ebay.com/sch/i.html?_from=R40&_nkw="
        link_tail = "+mens+watch&_sacat=0&LH_TitleDesc=0&_ipg=240&_pgn="
        return link_head+watchbrand+link_tail+str(pagenum+1)


    def mine(self):
        failed = 0
        with open('watches.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            #go through each keyword
            for keyword in self._keywords:
                
                for i in range(40):
                    try:
                        soup = BeautifulSoup(getHTMLdocument(self.get_search(keyword,i)), 'html.parser')
                        listings = soup.find("ul", {"class": "srp-results srp-grid clearfix"})\
                                    .find_all("div", {"class": "s-item__wrapper clearfix"})
                    except:
                        print(f"max of {i+1} pages for keyword '{keyword}'")
                        break

                    print(f"scraped page {i} of {keyword}")

                    #try to prevent too many API requests ban
                    time.sleep(0.75)

                    #get link from each listing
                    for listing in listings:
                        try:
                            link = listing.find("img")['src']
                            writer.writerow([link,keyword])
                        except:
                            failed += 1
                            continue
        if failed > 0:
            print(f"failed on {failed} listing(s)")
        
        print(f"successfully scraped 40 pages of {keyword}")

#uncommenting this code and running this file will result in a csv with 107,099 labeled watch images
miner = get_link_csv(['rolex','omega','seiko','invicta','hamilton','tissot','bulova','timex','elgin','unbranded','casio'])
miner.mine()

