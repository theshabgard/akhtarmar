import sdk
import json

userID = "619618"
apiKey = "181315b73871183a938f4c4b7aca89f5"

# make some dummy data in order to call vedic rishi api
data = {
    'date': 10,
    'month': 12,
    'year': 1993,
    'hour': 1,
    'minute': 25,
    'latitude': 25,
    'longitude': 82,
    'timezone': 5.5
}

# api name which is to be called
resource = "astro_details"

# instantiate VedicRishiClient class
client = sdk.VRClient(userID, apiKey)

# call horoscope apis
responseData = client.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'], data['latitude'], data['longitude'], data['timezone'])

loaded_json = json.loads(responseData.text)

print(loaded_json)  # <== prints json response.

print(loaded_json['ascendant'])  # <== prints single key