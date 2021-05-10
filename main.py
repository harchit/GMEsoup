import requests
import bs4
from bs4 import BeautifulSoup
from threading import Timer
from twilio.rest import Client
from credentials import auth_token, account_sid, my_cell, my_twilio
import time

client = Client(account_sid, auth_token)

def parseData():
    page = requests.get('https://finance.yahoo.com/quote/GME/')
    soup = bs4.BeautifulSoup(page.text, "lxml")
    price = soup.find('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

   
###
while True:
    price = float(parseData())
    print(price)
    time.sleep(1800)
    updated_price = float(parseData())
    print(updated_price)
    #get change in price 
    percent_change = 100*(updated_price - price) / price
     
     #send sms messa
    if (percent_change >= 10):
        message = "GME has changed by " + percent_change + "%"
        msg_twilio = client.messages.create(
        body= message,
        from_= my_twilio,
        to= my_cell
    )


