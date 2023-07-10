from deal_hunter.run import deal_hunter
import time

#Run this file to scrape 100 pages of ebay
TOKEN = "6357966637:AAEUtPeFnMUoNkJZFzg5C3NzanFddxD8vJw"
CHAT_ID = "5928330088"
KW = {"bulova", "seiko"}
KWD = {
       "bulova":50,
       "seiko":100,
       "rolex":500,
       "omega":200,
       "turtle":200,
       "hamilton":100,
       "padi":100,
       "lot":100,
      }
EBAY = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_sop=10&LH_BIN=1&_fsrp=1&rt=nc&LH_PrefLoc=3&_pgn="

for i in range(100):
      dh = deal_hunter(TOKEN,
                  CHAT_ID,
                  KWD,
                  EBAY+str(i))
      try:
            dh.send_listings()
      except:
            continue
      time.sleep(30)