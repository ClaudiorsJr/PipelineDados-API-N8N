import yfinance as yf

ticker = yf.Ticker("GC=F")

df = ticker.history(period="1d", interval="1m")

print(df)