api="469296086febdc90cb3294dab422b207"
LAT="19.905800"
LONG="83.164299"

import requests
from twilio.rest import Client

account_sid = 'AC6732f022baddf15356f59bc409a7254c'
auth_token = 'c00ab06c243b18bb90952205a762d45d'

parameter={
    "lat":LAT,
    "lon":LONG,
    "appid":api,
    "cnt":4

}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
curent_weather=response.json()

print(curent_weather['list'][0]['weather'][0]['id'])
will_rain=False
for hour_data in curent_weather["list"]:
    condition_code=hour_data["weather"][0]['id']
    if condition_code<700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='bring umbrella ☔ today',
        from_='+17086956184',
        to='+917751002939'
    )
    print(message.status)


else:
    print("there will be no rain")
