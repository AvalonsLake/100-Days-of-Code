import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ---- Stock Market API ---- #
stock_api_key = "TVIF2MQW5HLB4ZBE"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": stock_api_key,
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# ---- News API ---- #
news_api_key = "26f101b47ea24571bc823724357f33d4"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apikey": news_api_key,
}

# ---- Twilio API ---- #
account_sid = "ACd0305e3096e18d67a3dcf4e155524c42"
auth_token = "a52ac2ec87239463434cf35003595924"


# taking the JSON response and putting it into a list
closing_prices = [close_price for (date, close_price) in stock_data["Time Series (Daily)"].items()]
# Grabbing the last two days of closing prices
yesterday = float(closing_prices[0]["4. close"])
day_before_yesterday = float(closing_prices[1]["4. close"])
up_or_down = None
if yesterday > day_before_yesterday:
    up_or_down = "⬆️"
else:
    up_or_down = "⬇️"


# finding the percentage change between the last two days
daily_diff = abs(yesterday - day_before_yesterday)
percent_change = round(daily_diff / (day_before_yesterday * 0.01), 2)

if percent_change >= 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]
    formatted_articles = [f"{STOCK_NAME}: {up_or_down}{percent_change}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles[:3]]
    print(formatted_articles[1])
    # Texting the alert Via Twilio
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+18664777649",
            to="+18019718818"
        )
        print(message.status)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

