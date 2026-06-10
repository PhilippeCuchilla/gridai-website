import streamlit as st
from params import BASE_URL
import requests
from datetime import datetime
import folium
from streamlit_folium import st_folium
from folium import plugins
import datetime

st.markdown("""
<style>

/* Container des fées */
.fairy {
    position: fixed;
    font-size: 70px;
    z-index: 9999;
    pointer-events: none;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    animation-direction: alternate;
    opacity: 1;
}

/* Animations */
@keyframes fly1 {
    0% {
        transform: translate(-10vw, 90vh) rotate(0deg);
    }
    100% {
        transform: translate(110vw, -10vh) rotate(360deg);
    }
}

@keyframes fly2 {
    0% {
        transform: translate(100vw, 80vh) rotate(0deg);
    }
    100% {
        transform: translate(-20vw, 10vh) rotate(-360deg);
    }
}

@keyframes fly3 {
    0% {
        transform: translate(20vw, 100vh) rotate(0deg);
    }
    100% {
        transform: translate(80vw, -20vh) rotate(360deg);
    }
}

</style>

<div class="fairy" style="
    left:0%;
    animation: fly1 18s linear infinite;
">
⚡️
</div>

<div class="fairy" style="
    left:20%;
    animation: fly2 25s linear infinite;
    font-size:40px;
">
💡
</div>

<div class="fairy" style="
    left:50%;
    animation: fly3 20s linear infinite;
">
⚡️
</div>

<div class="fairy" style="
    left:70%;
    animation: fly1 30s linear infinite;
">
🔋
</div>

<div class="fairy" style="
    left:90%;
    animation: fly2 22s linear infinite;
">
🔋
</div>

""", unsafe_allow_html=True)

# Injecte le CSS
st.markdown("""
<style>
@keyframes flash {
    0%   { background: white; opacity: 0; transform: scale(0.8); }
    20%  { background: #fffde7; opacity: 1; transform: scale(1.05); }
    40%  { background: white; opacity: 0.8; }
    60%  { background: #fffde7; opacity: 1; transform: scale(1); }
    100% { background: transparent; opacity: 1; }
}

.prediction {
    animation: flash 1s ease-out forwards;
    padding: 20px;
    border-radius: 10px;
    font-size: 2em;
    text-align: center;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
st.set_page_config(layout="wide")
with col1:
    st.image("map_texas.png")
with col2 :
    with st.form(key='params_for_api'):
        predic_region = region = st.selectbox("Choisir une région", [ 'South Central', 'Coast', 'South', 'East','North Central', 'West', 'Far West', 'North'])
        predic_date = st.datetime_input('Date/Hour', value=datetime.datetime(2026, 5, 27, 7, 00, 00))
        st.form_submit_button('Make prediction', icon = '⚡️')

    code_regions = {
        "Coast" : "COAS",
        "East" : "EAST",
        "Far West" : "FWES",
        "North Central" : "NCEN",
        "North" : "NRTH",
        "South Central" : "SCEN",
        "South" : "SOUT",
        "West" : "WEST"
    }

    params = dict(
        region=code_regions[predic_region],
        date_time=str(predic_date)
        )

    gridai_api_url = f'http://127.0.0.1:8000/predict'
    URL_model = st.secrets['URL_machine']
    response = requests.get(URL_model, params=params)

    prediction = response.json()

    pred = round(prediction['prediction'],2)
    reel = round(prediction['reelle'],2)

    if prediction:
        st.markdown(f"""
            <div class="prediction">
                ⚡ {pred} MWh ⚡
            </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <div class="prediction">
                ⚡ {reel} MWh ⚡
            </div>
        """, unsafe_allow_html=True)
