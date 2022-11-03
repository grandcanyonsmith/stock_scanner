#!/usr/bin/env python3

import datetime
import random
import time
from urllib.request import urlopen

import matplotlib
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas_datareader.data as web
import pylab
from mplfinance.original_flavor import candlestick_ohlc
from pandas.core.common import flatten
from tabulate import tabulate
import sys
# from fool import Checker
import requests

from stock import Stock

# from main import *

while True:
# class Plot():
    matplotlib.rcParams.update({'font.size': 9})

    stocks = []

    # If stocks array is empty, pull stock list from stocks.txt file
    stocks = stocks or [line.rstrip() for line in open("stocks.txt", "r")]


    # Time frame you want to pull data from
    start = datetime.datetime.now()-datetime.timedelta(days=365)
    end = datetime.datetime.now()

    if __name__ == "__main__":
    # class Snn():

        # Array of moving averages you want to get
        MAarr = [20, 200]

        allData = []

        for ticker in stocks:

            try:
                data = []

                print(f"Pulling data for {ticker}")

                stock = Stock(ticker, start, end)

                data.extend((ticker.upper(), stock.closes[-1]))
                for MA in MAarr:
                    computedSMA = stock.SMA(period=MA)
                    # print(computedSMA)
                    data.append(computedSMA[-1])

                currentRsi = float("{:.2f}".format(stock.rsi[-1]))

                if currentRsi > 70 or currentRsi < 30:
                    data.append(str(currentRsi))
                    # data.append(str(currentRsi) + " 🔥")
                else:
                    data.append(currentRsi)

                chartLink = f"https://finance.yahoo.com/quote/{ticker}/chart?p={ticker}"

                data.append(chartLink)

                allData.append(data)

                            # Shows chart only if current RSI is greater than or less than 70 or 30 respectively
                            # if currentRsi < 30 or currentRsi > 70:

                            #     stock.graph(MAarr)

            except Exception as e:
                print('Error: ', e)

            # payload = tabulate(allData, headers=flatten([
            #     'Stock', 'Price', [str(x) + " MA" for x in MAarr], "RSI", "chart"]))
            rsi = str(currentRsi)
            total = f"{ticker} = "

            payload = {'stock': (total, currentRsi)}


        print(
            tabulate(
                allData,
                headers=flatten(
                    [
                        'Stock',
                        'Price',
                        [f"{str(x)} MA" for x in MAarr],
                        "RSI",
                        "chart",
                    ]
                ),
            )
        )



    # Checker()
    # time.sleep(10)  # Run once per 12 hours continuosly


# sys.exit()


