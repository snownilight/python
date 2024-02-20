import yfinance as yf
import pandas as pd
from datetime import datetime
from pandas import Timestamp

stockid = input('股票代碼： ')
stock = yf.Ticker(stockid + '.TW')
# stock = yf.Ticker('2330.TW')

dividend = round(stock.dividends, 1)

hash = {key: value for key, value in zip(dividend.index, dividend)}
rightHash = {}
nowYear = ''
sameYearDiv = 0

# add dividends from the same year
for k, v in hash.items():
    if nowYear != k.strftime('%Y'):
        sameYearDiv = 0
        nowYear = k.strftime('%Y')

    sameYearDiv += v
    rightHash[nowYear] = sameYearDiv

tenYearTotal = 0
for i in range(1, 11):
    tenYearTotal += list(rightHash.values())[-i]

average = tenYearTotal/10

print(f"平均股利：{average}")

safe = 0.8
cheap = round(average * 15 * safe, 2)
middle = round(average * 20 * safe, 2)
expensive = round(average * 30 * safe, 2)

print(f"便宜價：{cheap}")
print(f"中間價：{middle}")
print(f"昂貴價：{expensive}")