import sdk
import json
import streamlit as st

st.title('محسابه‌ی جزئیات اخترشناسانه‌ (وِدیک)')
from PIL import Image
import base64

image = Image.open('image.jpg')
st.image(image, caption='AkhtarMar')

day = st.number_input("روز تولد (میلادی)")
month = st.number_input("ماه تولد (میلادی)")
year = st.number_input("سال تولد (میلادی)")
hour = st.number_input("ساعت تولد (میلادی)")
minute = st.number_input("دقیقه‌ی تولد (میلادی)")
latitude = st.number_input("عرض جغرافیایی محل تولد")
longitude = st.number_input("طول جغرافیایی محل تولد")
timezone = st.number_input("Timezone of Birth")
function_list = ['birth_details', 'astro_details', 'planets', 'horo_chart/:SUN', 'horo_chart/:D1',
                 'horo_chart_image/:D1']
resource = st.sidebar.selectbox("لطفاً کارکرد مدنظر خود را وارد کنید", function_list)

data = {
    'date': day,
    'month': month,
    'year': year,
    'hour': hour,
    'minute': minute,
    'latitude': latitude,
    'longitude': longitude,
    'timezone': timezone,
}


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)


# instantiate VedicRishiClient class
client = sdk.VRClient("619618", "181315b73871183a938f4c4b7aca89f5")

responseData = client.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'],
                           data['latitude'], data['longitude'], data['timezone'])

loaded_json = json.loads(responseData.text)
if resource == 'horo_chart_image/:D1':
    render_svg(loaded_json)

print(loaded_json)  # <== prints json response.
st.write(loaded_json)
