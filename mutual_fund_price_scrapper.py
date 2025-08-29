import os
import sys
import requests
import csv
import pandas as pd
import datetime
import schedule
import time

from bs4 import BeautifulSoup

def read_mutual_fund_file():
    with open('my_mutual_funds.csv', 'r') as stock_data_file:
        return stock_data_file.readlines()
 
def get_mutual_fund_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; FundPriceBot/1.0; +http://yourwebsite.com/bot)"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    # Adjust this selector if needed
    price_span = soup.find("span", class_="open-price-value")
    if price_span:
        return price_span.get_text(strip=True)
    else:
        raise ValueError("Could not find the price element on the page.")
     
def write_mutual_fund_price():
    list_of_stock_stickers =[]
    list_of_stock_prices = []
    stock_tickers = read_mutual_fund_file()
    for stock in stock_tickers:
        try:
            print("Stock",stock)
            
            url = "https://www.theglobeandmail.com/investing/markets/funds/%s/"%(stock.strip())
            print (url)
                     
            price = get_mutual_fund_price(url)
            if price:
                print("Stock :",stock," stock price: ", price)
                list_of_stock_stickers.append(stock.strip())
                list_of_stock_prices.append(price)
                time.sleep(5)
            else:
                 print("Stock price element not found.")
        except Exception as error:
            print("An error occured",error.args[0])
            sys.exit()
    print(list_of_stock_stickers)
    data_t = {'stock': list_of_stock_stickers,'price': list_of_stock_prices}
    df = pd.DataFrame.from_dict(data_t)
    df.to_excel("mutual_prices.xlsx")

# Schedule job every 10 minutes
schedule.every(10).minutes.do(write_mutual_fund_price)

print("Scheduler started... running every 10 minutes.")
while True:
    schedule.run_pending()
    time.sleep(60)




 

