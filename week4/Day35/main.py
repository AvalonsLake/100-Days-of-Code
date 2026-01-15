import requests
from twilio.rest import Client

account_sid = "AC38d362c73825e086cd48be8a41cc624e"
auth_token = "62c8991e5ffc40fd8dc1f049a49ad762"

api_key = "2d6a22383efb2986fd31aa8c9d593bb2"
parameters = {
    "lat": 40.760780,
    "lon": -111.891045,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = True
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+15163631765",
        to="+18019718818"
    )
    print(message.status)