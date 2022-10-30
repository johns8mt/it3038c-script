#I chose to go with Macys because Dicks and American Eagle both blocked me after trying my script two times to test it.
#If I did this again instead of getting clothing information I think I would rather build something useful like Covid Case numbers or something with an actual use.

import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.macys.com/shop/product/tommy-hilfiger-mens-custom-fit-ivy-polo?ID=1990894").content 
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"page-header simple product-title large"})
title = span.text
span = soup.find("span", {"class":"money"})
price = span.text
span2 = soup.find("div", {"class":"form-field form-field-swatch swatch-other"})
colors = span2.text
print("Item %s has the price %s" % (title, price))

#Example of the output from the script is below: 
#Men's Custom-Fit Ivy Polo has price of $39.99
