from bs4 import BeautifulSoup
import requests

# Scraping Crypto prices
# I don't support crypto but this was the website the tutorial showed + limited websites that allow web scraping

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# next element
# print(trs[0].next_sibling)

# prev element
#print(trs[1].previous_sibling)

# all next siblings
#print(list(trs[0].next_siblings))

# get the tag above selected element
# print(trs[0].parent)

# get everything inside tag
# print(list(trs[0].children))

prices = {}

# search for names and prices in the tables
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixedName = name.p.string
    fixedPrice = price.a.string

    prices[fixedName] = fixedPrice

print(prices)