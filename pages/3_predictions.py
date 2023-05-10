import streamlit as st
import pickle
import pandas as pd
import numpy as np
from pages.static.helper import translation
from util import Retreiving_Details
import time
st.set_page_config(
    layout="wide", initial_sidebar_state="collapsed", page_icon="🔮")

with open('pages/static/custom_homepage.css') as pgdesign:
    st.markdown(f"<style> {pgdesign.read()}</style>", unsafe_allow_html=True)
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


# getting the model and loading it
df_gdp = pd.read_csv('pages/datasets/GDP.csv')
prediction = pickle.load(open("pages//static//NavieBayes.pkl", "rb"))
# reading the csv file
df_pred = pd.read_csv('pages/static/crop_recommendation.csv')
columns = df_pred.columns[0:6]
st.markdown("""
<h1 style="color: #333; font-family: 'Comic Sans MS', sans-serif; font-size: 35px; font-weight: bold; transition: color 0.1s ease-in-out;"
><span style="display: inline-block; transition: color 0.3s ease-in-out;"
>Know What To Grow</span>🌾</h1>
""", unsafe_allow_html=True)
with open("pages/static//vizcss.css") as h:
    st.markdown(f"<style> {h.read()}</style>", unsafe_allow_html=True)
# heading of our page
st.components.v1.html("""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Typewriter Effect</title>
    <style>
      /* Add some basic styling */
      #typewriter {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        text-align: center;
	    font-weight: bold;
        color: #8BC34A;
	
        white-space: nowrap;
        overflow: hidden;
        border-right: 1px solid black;
        padding:0;
      }
    </style>
  </head>
  <body>
    <!-- Add an empty div to display the typewriter effect -->
    <div id="typewriter"></div>

    <!-- Add a script to create the typewriter effect -->
    <script>
      var text = "Make Sure to Enter the Values in Ratio's of Each Other! "; // Replace with your own text
      var i = 0;
      var speed = 90; // Adjust typing speed in milliseconds

      function typeWriter() {
        if (i < text.length) {
          document.getElementById("typewriter").innerHTML += text.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }
      }

      // Call the typeWriter function when the page loads
      window.onload = function() {
        typeWriter();
      };
    </script>
  </body>
</html>
""")

st.markdown("<a href=https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/fertilizer-numbers-npk.htm>Example</a>", unsafe_allow_html=True)

val1, val2 = st.columns(2)
with val1:
    state = st.selectbox(label='***Select the Indian State*** ',
                         options=df_gdp['State Name'].unique())
    n = st.number_input(
        "**Nitrogen**", min_value=df_pred['N'].min(), max_value=df_pred['N'].max())
    k = st.number_input('**Potassium**',
                        min_value=df_pred['K'].min(), max_value=df_pred['K'].max())

with val2:
    a = df_gdp['State Name'] == state
    dist = df_gdp.loc[a, 'Dist Name']
    dist = st.selectbox(label='***Select The District***',
                        options=dist.unique())
    p = st.number_input('**Phosphorus**', min_value=df_pred['P'].min(),
                        max_value=df_pred['P'].max())
    type_crop = st.text_input('**Crop You Want To Grow**',
                              max_chars=20, placeholder='Optional', key="crop_type")

button = st.button('Predict')


if button:
    # to run a progress bar and make the app asthetic
    st.balloons()

    # we need 7 features as input - got 3 from user taking other inputs as random each time submit is clicked
    temperature = np.array(df_pred['temperature'].sample(
        random_state=np.random.randint(0, high=len(df_pred['N']))))[0]

    ph = np.array(df_pred['ph'].sample(
        random_state=np.random.randint(0, high=len(df_pred['N']))))[0]

    humidity = np.array(df_pred['humidity'].sample(
        random_state=np.random.randint(0, high=len(df_pred['N']))))[0]

    rainfall = np.array(df_pred['rainfall'].sample(
        random_state=np.random.randint(0, high=len(df_pred['N']))))[0]
    values = [[n, p, k, temperature, ph, humidity, rainfall]]

    prediction = prediction.predict(values)
    i = np.random.randint(low=0, high=len(df_pred['ph']))
    crop = df_pred['label'][i]
    st.subheader(
        f':smile: Your Farm is Suitable for Growing {crop}')

if type_crop:  # optional parameter to grow the crop is given by the user then this condition is True
    bar = st.progress(
        2, text=":heart: Please wait! **We Appreciate Your Patience**")
    # call the api here and let it load until the bar is finished then print it later
    question = []
    question.append(
        {'role': 'system',
         'content': f"What should I do If I want to Grow {type_crop} in my farm in {state} in the {dist} district,\
                    with the values of fertilizer's of proportions as nitrogen:**{n}**,phosphorus:**{p}**,and pottasium:**{k}**?"})
    question = Retreiving_Details(question)
    for percent_complete in range(100):
        time.sleep(0.0001)
        bar.progress(percent_complete, text=":heart: Please wait!")
    st.subheader(f"To Grow {type_crop} You can do The following 👇")
    # # adding this in the drop down  for better readibility
    st.write('{0}\n'.format(
        question[-1]['content'].strip()))


