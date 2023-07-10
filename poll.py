from deal_hunter.run import deal_hunter
import time

#run this file if you want watchbot to run in perpituity


# Look into how to make a Telegram watchbot link: https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/
# After you have made your bot, plug in the TOKEN and CHAT_ID variables here
# 

TOKEN = "YOUR BOT'S UNIQUE TOKEN"
CHAT_ID = "YOUR CHAT ID"
KWD = {
        # replace these with the keywords you would like to search for
       "bulova":50,
       "seiko":100,
       "rolex":1200,
       "omega":300,
       "turtle":200,
       "hamilton":100,
       "padi":100,
       "lot":100,
      }

#replace these with keywords you don't want results from
NEGATIVE_KWS = {"women","women's","lady","lady's","quartz","ladies","womens","mickey"}

#replace this with the ebay page you would like to scrape from
#customize location, items per page, and any other configs on ebay before copying link
EBAY = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=watch&_sacat=0&_sop=10&LH_BIN=1&_fsrp=1&rt=nc&LH_PrefLoc=3&_ipg=240"
dh = deal_hunter(TOKEN,
                    CHAT_ID,
                    KWD,
                    EBAY,
                    NEGATIVE_KWS)
i = 0
while True:
    i += 1
    dh.send_listings()
    time.sleep(30)
    print(f"iteration: {i}")