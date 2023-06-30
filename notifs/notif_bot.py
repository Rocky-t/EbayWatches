import requests
from datetime import datetime
import time
import sys
sys.path.insert(1,"../")
from listing_obj.listing import lo


class EbayScanner:
    def __init__(self, token, chat_id):
        self._token = token
        self._chat_id = chat_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chat_id}&text={message}"
        requests.get(url).json() # this sends the message

    def alert(self,item:lo):
        now = datetime.now()
        self.send_message(item.summary())
        self.send_message("Here's the link:")
        self.send_message(item._link)
        print("listing sent at:",now.strftime("%d/%m/%Y %H:%M:%S"))
