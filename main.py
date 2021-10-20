import requests
from twilio.rest import Client

# twilio account details
account_sid = "ksfdskpfodskflksddslkjfsd"
auth_token = "dskjfhdsoihovzdhxkjdskj"

parameters = {
    # add app id from openweatherapp
    "appid": "102930942398238950932",
    # your latitude here
    "lat": 1,
    # your longitude here
    "lon": 1,
    "exclude": "current,daily,minutely",
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
weather_slice = data[:10]
will_rain = False
for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "Bring an umbrella it looks like rain today.",
        from_="+111111111",
        to="+00000000000"
    )
    print(message.status)
