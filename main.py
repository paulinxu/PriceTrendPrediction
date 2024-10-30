import yfinance as yf

print("starting")

appl = yf.Ticker("APPL")

# get all stock info
print(appl.info)

# get historical market data
hist = appl.history(period="1mo")
print(hist)

print(appl.news)
