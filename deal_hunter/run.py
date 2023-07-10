import sys
sys.path.insert(1,"../")
from scrape.get_listings import ebay_getter
from listing_obj.listing import lo
from notifs.notif_bot import EbayScanner

class deal_hunter:
    """
    A class to contain all moving parts of the watch bot. Just initialize the object then call send_listings
    """
    def __init__(self,
                token,
                chat_id,
                keywords,
                ebay_link,
                negative_keywords):
        self._ebg = ebay_getter(link=ebay_link,keywords=keywords,negative_keywords=negative_keywords)
        self._ebs = EbayScanner(token=token,chat_id=chat_id)

    def send_listings(self):
        listings = self._ebg.get_listings()
        for listing in listings:
            self._ebs.alert(listing)