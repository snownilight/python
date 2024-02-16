import yfinance as yf
import pandas as pd
from datetime import datetime
from pandas import Timestamp

stockid = input('股票代碼： ')
stock = yf.Ticker(stockid + '.TW')
# stock = yf.Ticker('2330.TW')

dividend = round(stock.dividends, 1)
data = pd.DataFrame(dividend)

data = data.reset_index()
data.columns = ['日期', '股利']

# for item in dividend:
    

# for item2 in dividend.index:
#     print(item2)

hash = {key: value for key, value in zip(dividend.index, dividend)}
rightHash = {}
nowYear = ''
sameYearDiv = 0

## TODO:last year doesn't append to righthash

for k, v in hash.items():
    if nowYear != '' and nowYear != k.strftime('%Y'):
        rightHash[nowYear] = sameYearDiv
        sameYearDiv = 0

    sameYearDiv += v
    nowYear = k.strftime('%Y')


print(rightHash)




# print(data)

# average = data['股利'].tail(10).mean()

# print(f"平均股利：{average}")

# safe = 0.8
# cheap = round(average * 15 * safe, 2)
# middle = round(average * 20 * safe, 2)
# expensive = round(average * 30 * safe, 2)

# print(f"便宜價：{cheap}")
# print(f"中間價：{middle}")
# print(f"昂貴價：{expensive}")