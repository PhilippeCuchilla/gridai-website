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

st.set_page_config(layout="wide",page_title="Grid-AI Prediction", page_icon="⚡️")
st.title("⚡️ Grid-AI ⚡️",text_alignment="center")
st.subheader("Global Real-time Intelligent Demand AI", text_alignment="center", divider= 'grey')

create_page = st.Page("page_machine.py", title="Machine Learning", icon="🌳")
delete_page = st.Page("page_deep.py", title="Deep Learning", icon="🧠")

pg = st.navigation([create_page, delete_page], position = 'top')
pg.run()
