import sys
sys.path.insert(1,"../")
from scrape.get_listings import ebay_getter
from listing_obj.listing import lo
from notifs.notif_bot import EbayScanner

TOKEN = "6357966637:AAEUtPeFnMUoNkJZFzg5C3NzanFddxD8vJw"
CHAT_ID = "5928330088"
KW = {"bulova", "seiko5",}
EBAY = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_sop=10&LH_BIN=1&rt=nc&_udhi=100"

class deal_hunter:
    def __init__(self,
                token=TOKEN,
                chat_id=CHAT_ID,
                keywords=KW,
                ebay_link=EBAY):
        self._token = token
        self._chat_id = CHAT_ID
        self._keywords = keywords
        self._ebay_link = ebay_link

    def send_listings(self):
        print("start scrape")
        ebg = ebay_getter(link=self._ebay_link,keywords=self._keywords)
        ebs = EbayScanner(token=self._token,chat_id=self._chat_id)
        listings = ebg.get_listings()

        for listing in listings:
            ebs.alert(listing)