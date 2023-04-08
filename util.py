import requests
import openai
import os
import json
import streamlit as st


@st.cache_data
def lottie_load_json(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


# system assistant and user there will be 3 roles.

@st.cache_data
def Retreiving_Details(conversation):
    apikey = st.secrets["api_key"]  # os.getenv("API_KEY")
    openai.api_key = apikey
    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation
    )
    conversation.append(
        {'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation
