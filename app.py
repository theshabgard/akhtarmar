import sdk
import json
import streamlit as st

st.title('Vedic Astrology App')
day = st.number_input("Day of Birth")
month = st.number_input("Month of Birth")
year = st.number_input("Year of Birth")
hour = st.number_input("Hour of Birth")
minute = st.number_input("Minute of Birth")
latitude = st.number_input("Latitude of Birth")
longitude = st.number_input("Longitude of Birth")
timezone = st.number_input("Timezone of Birth")

resource = "astro_details"
data = {
    'date': day,
    'month': month,
    'year': year,
    'hour': hour,
    'minute': minute,
    'latitude': latitude,
    'longitude': longitude,
    'timezone': timezone
}
# instantiate VedicRishiClient class
client = sdk.VRClient("619618", "181315b73871183a938f4c4b7aca89f5")
responseData = client.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'],
                           data['latitude'], data['longitude'], data['timezone'])

loaded_json = json.loads(responseData.text)

print(loaded_json)  # <== prints json response.
st.write(loaded_json)

