from datetime import datetime
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import os
from zipfile import ZipFile
from stocks import dev

def get_stocks(stock, start_dt, end_dt, id): 
    DNE_list = []
    before_list = []
    
    if (end_dt-start_dt).days <= 0:
        return "Error", before_list
    
    stock_list = stock.split(',')
    with ZipFile('sampleDir%s.zip' % id, 'w') as zipObj:
        for stocks in stock_list:
            stocks = stocks.replace(" ", "")
            try: 
                df = pdr.data.get_data_yahoo(stocks, start=start_dt, end=end_dt)

                """Check for date < start_dt"""
                time_str = str(df.index.values[0]).replace('T00:00:00.000000000', '')
                time = datetime.strptime(time_str, "%Y-%m-%d")
                if time.toordinal() > start_dt.toordinal()+7:
                    before_list.append(stocks)

                df.to_csv('%s.csv' % stocks)
                zipObj.write('%s.csv' % stocks)
            except:
                DNE_list.append(stocks)

    if dev:
        for stocks in stock_list:
            try:
                stocks = stocks.replace(" ", "")
                os.remove('%s.csv' % stocks)
            except:
                pass

    return DNE_list, before_list