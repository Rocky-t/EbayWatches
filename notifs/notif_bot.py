import requests
from datetime import datetime
import time
import sys
sys.path.insert(1,"../")
from listing_obj.listing import lo


class EbayScanner:
    """This class holds all the pieces needed to send a message to my phone (or anyone else's)"""
    def __init__(self, token, chat_id):
        self._token = token
        self._chat_id = chat_id

    def send_message(self, message):
        url = f"https://api.telegram.org/bot{self._token}/sendMessage?chat_id={self._chat_id}&text={message}"
        requests.get(url).json() # this sends the message
        print("message sent at:",datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    def alert(self,item:lo):
        self.send_message(item.summary() + '\n'+ "Here's the link: \n" + item._link)
