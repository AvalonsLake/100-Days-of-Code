from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import smtplib
import os

load_dotenv()

# Variables
goal_price = 120.00
email = os.getenv("EMAIL")
password = os.getenv("PASS")
smtp_address = os.getenv("SMTP_ADDRESS")

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",

  }

product_url = "https://www.amazon.com/GAOMON-PD1161-11-6-inch-Battery-Free-Animation/dp/B07YFG742J?dib=eyJ2IjoiMSJ9.aB24arHJD0C0OlEM1U5uhf437ln0VCPeRHAxSYZ4TTj1knA-92WePKYgOkYziV5HdvWXELdnKuwn8azfFt0QsbsKdD2JDyCOcgzbXejd0sSEMa84S9v4mU2ajMX-kJW9r_PYmDcTKU7AmayWXYfPwaQsZ1Mgidg_g52F0vmsz5PyfXwJXaBQQDQ9KNL-hcEPkqcr5kxzUA4DvExs5R3cOSL07rR8_puIE7DfHu8esbE.ZlxyJq3mvc1BPQmm5SlWsix1-EixiGiZh94M-kmybVw&dib_tag=se&keywords=art%2Btablet&qid=1769622294&sr=8-6&th=1"

response = requests.get(product_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Grab the price and convert to floating integer
price_whole = soup.select_one("span.a-price-whole")
price_decimal = soup.select_one("span.a-price-fraction")
price = float(price_whole.getText() + price_decimal.getText())

# Grab the product Title
title = soup.select_one("span.product-title-word-break").getText()

print(price)
print(title)

# Email user when price drops below the goal_price
if price < goal_price:
    with smtplib.SMTP(smtp_address, port=587) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs="jlh3ndr@gmail.com",
            msg=f"{title} is now ${price}. Here's the link to buy it! \n"
                f"{product_url}".encode('utf-8')
        )
    print("message sent... Hopefully")