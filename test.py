from deal_hunter.run import deal_hunter

TOKEN = "6357966637:AAEUtPeFnMUoNkJZFzg5C3NzanFddxD8vJw"
CHAT_ID = "5928330088"
KW = {"bulova", "seiko"}
KWD = {
       "bulova":50,
       "seiko":100,
       "rolex":500,
       "omega":200,
       "prospex":200,
      }
EBAY = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_sop=10&LH_BIN=1&rt=nc&_udhi=100"

dh = deal_hunter(TOKEN,
                CHAT_ID,
                KW,
                EBAY)
dh.send_listings()