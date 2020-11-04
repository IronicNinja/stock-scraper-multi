from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import os
from zipfile import ZipFile
from stocks import dev
from flask import Flask

def get_stocks(stock, start_dt, end_dt): 
    """
    time_diff = end_dt - start_dt
    if time_diff.days < 0:
        raise Exception("Start date is after end date.")
    """
    stock_list = stock.split(',')

    with ZipFile('sampleDir.zip', 'w') as zipObj:
        for stocks in stock_list:
            stocks = stocks.replace(" ", "")
            df = pdr.data.get_data_yahoo(stocks, start=start_dt, end=end_dt)
            #path = r'C:\Users\evanz\Desktop\stock_scraper\stocks\downloads'
            #df.to_csv(os.path.join(path, r'%s.csv' % stocks))
            #zipObj.write(path, basename(filePath))
            df.to_csv('%s.csv' % stocks)
            zipObj.write('%s.csv' % stocks)

    if dev:
        for stocks in stock_list:
            stocks = stocks.replace(" ", "")
            os.remove('%s.csv' % stocks)


get_stocks('FB, GOOG', '2020-01-05', '2020-01-20')