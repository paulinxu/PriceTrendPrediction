import yfinance as yf
import time

from transformers import pipeline
import torch

from timeformat import print_time

device = 'cuda' if torch.cuda.is_available() else 'cpu'

sentiment_pipeline = pipeline("text-classification", model="mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis",  device=device)

# sentiment_pipeline2 = pipeline("sentiment-analysis", device=device)

print("starting")


# get stock price

# for i in range(0, 30):

#     stock = yf.Ticker("MSFT")
#     print(stock.info["currentPrice"])
#     time.sleep(1)

# print("-------------------------------")
# # get historical market data

stock = yf.Ticker("APPL")

for article in stock.news:
    print("==================================")
    title = article["title"]
    print(title)
    publishTime = article["providerPublishTime"]
    print_time(publishTime)
    print(article["link"])
    print("--------------------")
    print("Title sentiment: ")
    data = [title]
    print(sentiment_pipeline(data))
    print("----------------------")
    print("Price change")
    hist = stock.history(interval="5m", start=publishTime, end=publishTime + 5 * 60 * 12)
    # hist = stock.history(interval="30m", period="1d")
    print(hist)



# print(hist)
# for article in stock.news:
#     print("-------------------------------")
#     print(article["title"])
#     print(article["providerPublishTime"])
#     print(article["link"])



