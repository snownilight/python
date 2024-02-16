import pandas as pd
import yfinance as yf
import ta

# 下载股票数据
def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# 计算并添加指标
def calculate_indicators(data):
    # 计算移动平均线
    data['SMA_20'] = ta.trend.sma_indicator(data['Close'], window=20)
    data['SMA_50'] = ta.trend.sma_indicator(data['Close'], window=50)

    # 计算相对强度指标 (RSI)
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=14).rsi()

    return data

# 绘制图表
def plot_chart(data):
    data[['Close', 'SMA_20', 'SMA_50']].plot(title='Stock Price and Moving Averages')
    data['RSI'].plot(secondary_y=True, title='RSI')

    # 添加图例
    import matplotlib.pyplot as plt
    plt.legend(['Close', 'SMA_20', 'SMA_50', 'RSI'])

    # 显示图表
    plt.show()

# 主函数
def main():
    ticker = '2330.TW'  # 选择要分析的股票
    start_date = '2024-01-01'
    end_date = '2024-02-16'

    # 下载股票数据
    stock_data = download_stock_data(ticker, start_date, end_date)

    # 计算指标
    stock_data = calculate_indicators(stock_data)

    # 绘制图表
    plot_chart(stock_data)

if __name__ == "__main__":
    main()
