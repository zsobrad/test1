%matplotlib inline
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data
def fetch_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

tickers = ['^VIX', 'SPY']
start_date = '2020-01-01'
end_date = '2023-12-31'
data = fetch_data(tickers, start_date, end_date)

# Calculate returns
def calculate_returns(data):
    returns = data.pct_change().dropna()
    return returns

returns = calculate_returns(data)

# Plot price data
def plot_price_data(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['SPY'], label='SPY')
    plt.plot(data.index, data['^VIX'], label='VIX')
    plt.title('SPY and VIX Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_price_data(data)

# Plot returns
def plot_returns(returns):
    plt.figure(figsize=(14, 7))
    plt.plot(returns.index, returns['SPY'], label='SPY')
    plt.plot(returns.index, returns['^VIX'], label='VIX')
    plt.title('SPY and VIX Daily Returns')
    plt.xlabel('Date')
    plt.ylabel('Daily Returns')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_returns(returns)

# Plot correlation
def plot_correlation(returns):
    correlation = returns.corr()
    print("Correlation between SPY and VIX daily returns:\n", correlation)
    plt.figure(figsize=(6, 5))
    plt.matshow(correlation, cmap='coolwarm', fignum=1)
    plt.colorbar()
    plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=90)
    plt.yticks(range(len(correlation.columns)), correlation.columns)
    plt.title('Correlation Matrix')
    plt.show()

plot_correlation(returns)
