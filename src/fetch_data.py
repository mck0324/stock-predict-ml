# down load data from yfinance
import yfinance as yf

def fetch_data(ticker="SPY"):
    df = yf.download(ticker, start="2018-01-01", end="2024-01-01")
    df.to_csv(f"data/{ticker}.csv")
    return df