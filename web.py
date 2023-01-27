import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import time

# Import some bits
import ephem, math, datetime
from datetime import datetime
# Get retina display quality for plots

home = ephem.Observer()
# Set up
home.date = datetime.now()
home.lat = '3.5201'
home.lon = '98.4321'

sun = ephem.Sun()
sun.compute(home)

st.set_page_config(page_title='altair21')
st.header('altair_pk.lab')
st.write(""" Selamat datang di website sederhana ini ! """)
st.write(""" web ini masih dalam tahap pengembangan dan sebatas percobaan""")
st.write("---")

st.sidebar.success("select a page above")

st.write("##")
st.metric("Location", "Balai Kasih")
st.write("### Waktu :", datetime.now())
col1, col2, col3 = st.columns(3)

rising = home.previous_rising(sun).datetime()
col1.metric("Waktu Terbit Matahari     :", f"{(rising.hour+7)-24} : {rising.minute} : {rising.second}")

transit = home.next_transit(sun).datetime()
col2.metric("Waktu Transit Matahari    :", f"{(transit.hour+7)} : {transit.minute} : {transit.second}")

setting = home.next_setting(sun).datetime()
col3.metric("Waktu Terbenam Matahari   :", f"{(setting.hour+7)} : {setting.minute} : {setting.second}")

#while True:
#url = 'http://api.open-notify.org/iss-now.json'
#df = pd.read_json(url)
#df['latitude'] = df.loc['latitude', 'iss_position']
#df['longitude'] = df.loc['longitude', 'iss_position']
#df.reset_index(inplace=True)

#df = df.drop(['index', 'message'], axis=1)
    
#st.dataframe(df)

#fig = px.scatter_geo(df, lat='latitude', lon='longitude')
#fig.show()
#st.write(""" 
### ISS Live Position""")
#st.plotly_chart(fig)
#timesleep(5)

#############################################################################################

###############################################################################################

#############################################################################################################################

#x = st.slider("Select an integer x", 0, 10, 1)
#y = st.slider("Select an integer y", 0, 10, 1)

#d = pd.DataFrame({"x": [x], "y": [y], "x + y": [x + y]}, index = ["addition row"])
#st.write(d)
############################################################################################################################


import requests

api_key = "799ecc7e8c9d4cdabdd14550230801"
base_url = "http://api.weatherapi.com/v1"
city = "Dalan Naman"

parameters = {"key":api_key, "q":city}         # URL parameters
r = requests.get(f"{base_url}/current.json", params=parameters)

data = r.json()         # retrieve the json data

location = data['location']['name']
time = data['location']['localtime']

condition = data['current']['condition']['text']     
temperature_celcius = data['current']['temp_c']
temperature_farenheit = data['current']['temp_f']
feelslike_celcius = data['current']['feelslike_c']
wind_direction = data['current']['wind_dir']
humidity = data['current']['humidity']

st.write("## ")

# printing data

col1, col2, col3 = st.columns(3)
col1.metric(label='Temperature', value=f"{temperature_celcius} °C" )
col2.metric("Feels like", f"{feelslike_celcius} °C")
col3.metric("Humidity", f"{humidity} %")

st.metric('Weather Condition',f'{condition}')
st.write(f"Wind Direction: {wind_direction}")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
     <form action="https://formsubmit.co/kawakibialtair@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
     </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
 
