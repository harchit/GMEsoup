import requests
import bs4
from bs4 import BeautifulSoup
from threading import Timer

def parseData():
    page = requests.get('https://finance.yahoo.com/quote/GME/')
    soup = bs4.BeautifulSoup(page.text, "lxml")
    price = soup.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

#every hour get price data
t = Timer(60*60, parseData)




