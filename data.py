import yfinance as yf

df = yf.download("SPY", start="2018-01-01", end="2024-01-01")
df.head()
print(df.head())
print("df shape: ", df.shape)
