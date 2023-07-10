from deal_hunter.run import deal_hunter
import time

#run this file if you want watchbot to run in perpituity

TOKEN = "6357966637:AAEUtPeFnMUoNkJZFzg5C3NzanFddxD8vJw"
CHAT_ID = "5928330088"
KW = {"bulova", "seiko"}
KWD = {
       "bulova":50,
       "seiko":100,
       "rolex":1200,
       "omega":300,
       "turtle":200,
       "hamilton":100,
       "padi":100,
       "lot":100,
      }
EBAY = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_sop=10&LH_BIN=1&_fsrp=1&rt=nc&LH_PrefLoc=3&_ipg=240"
dh = deal_hunter(TOKEN,
                    CHAT_ID,
                    KWD,
                    EBAY)
i = 0
while True:
    i += 1
    dh.send_listings()
    time.sleep(30)
    print(f"iteration: {i}")