import streamlit as st
from params import BASE_URL
import requests
from datetime import datetime
import folium
from streamlit_folium import st_folium
from folium import plugins


st.set_page_config(page_title="Grid-AI Prediction", page_icon="⚡️", layout="centered")
st.title("⚡️ Grid-AI")
st.markdown("### Global Real-time Intelligent Demand AI")


with st.form(key='params_for_api'):
    predic_region = st.text_input('Texas Region', value='COS')
    predic_date = st.date_input('date', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    predic_time = st.time_input('time', value=datetime.datetime(2012, 10, 6, 12, 10, 20))
    predic_datetime = f'{pickup_date} {pickup_time}'

    st.form_submit_button('Make prediction')

params = dict(
    predic_region=predic_region,
    predic_datetime=predic_datetime
    )

gridai_api_url = 'https://gridaiURL/predict'
response = requests.get(gridai_api_url, params=params)

prediction = response.json()

pred = prediction['']

st.header(f'Electricty prevision need: ${round(pred, 2)}')
